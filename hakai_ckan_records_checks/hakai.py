import difflib
import functools
import json
import os
import re
from datetime import date

import pandas as pd
import requests
from loguru import logger

ORGANIZATIONS = [
    "Hakai Institute",
]
DOI_CODE_FORMAT = r"https\:\/\/doi\.org"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO_URL_RE = re.compile(r"^https?://github\.com/([^/]+)/([^/]+?)(?:/.*)?$")
ERDDAP_RESOURCE_URL_RE = re.compile(r"^(https?://[^/]+/erddap)/(?:tabledap|griddap|info)/([^./]+)")
_github_session = requests.Session()
_erddap_session = requests.Session()

_SKIP_URL_PREFIXES = (
    "https://cioos.ca/translation_method",
    "http://standards.iso.org",
    "https://standards.iso.org",
    "https://www.iana.org",
    "http://www.w3.org",
    "https://www.w3.org",
    "https://creativecommons.org",
    "https://en.wikipedia.org",
    "https://epsg.org",
    "http://wiki.esipfed.org",
    "https://wiki.esipfed.org",
    "http://www.opengis.net",
    "https://www.opengis.net",
    "https://schemas.isotc211.org",
)


def _normalize_name(name):
    if "," in name:
        parts = [p.strip() for p in name.split(",", 1)]
        name = f"{parts[1]} {parts[0]}"
    normalized = re.sub(r"\s+[A-Za-z]\.\s*", " ", name).strip()
    return re.sub(r"\s+", " ", normalized)


def _fuzzy_match(a, b, threshold=0.85):
    if not (a and b):
        return False
    return difflib.SequenceMatcher(None, _normalize_name(a.lower()), _normalize_name(b.lower())).ratio() >= threshold


def _github_owner_repo(match):
    """Extract a lowercased (owner, repo) tuple from a GITHUB_REPO_URL_RE match, or None."""
    return (match.group(1).lower(), match.group(2).lower()) if match else None


def _date_by_type(entries, date_type):
    return next((d["value"] for d in entries if d.get("type") == date_type), None)


@functools.cache
def _get_latest_github_release_date(owner, repo):
    """Fetch the published date of a GitHub repo's latest release, or None if unavailable."""
    headers = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    try:
        response = _github_session.get(
            f"https://api.github.com/repos/{owner}/{repo}/releases/latest",
            headers=headers,
            timeout=15,
        )
        if response.status_code != 200:
            return None
        return date.fromisoformat(response.json()["published_at"][:10])
    except (requests.exceptions.RequestException, KeyError, ValueError):
        return None


@functools.cache
def _get_erddap_last_data_date(erddap_base, dataset_id):
    """Fetch the date of the most recent 'time' data point in an ERDDAP tabledap dataset, or None if unavailable."""
    try:
        response = _erddap_session.get(
            f'{erddap_base}/tabledap/{dataset_id}.json?time&orderByMax(%22time%22)',
            timeout=60,
        )
        if response.status_code != 200:
            return None
        return date.fromisoformat(response.json()["table"]["rows"][0][0][:10])
    except (requests.exceptions.RequestException, KeyError, IndexError, ValueError):
        return None


@logger.catch(default=pd.DataFrame())
def test_record_requirements(record) -> pd.DataFrame:
    def _test(condition, message):
        if not condition:
            logger.debug(message)
            results.append([message])

    results = []
    logger.debug("Review Record {}", record["id"])

    # Organization
    _test("organization" in record, "No organization")
    _test(
        record["organization"]["title"] in ORGANIZATIONS,
        f"Unknown organization title: {record['organization']['title']}",
    )
    _test(any(record.get("projects") or []), "No projects associated")
    _test(
        [
            uri
            for uri in record["organization"]["organization-uri"]
            if uri["authority"] == "ROR"
        ],
        "Organization is missing an ROR URI",
    )

    # Licence
    _test(record.get("license_id") != "", "Empty licence")

    # Version
    citation = json.loads(record["citation"]["en"].replace('\\"', '"'))
    version = citation[0].get("version")
    is_tentative = (record.get("progress") or "").lower() == "tentative"
    if is_tentative:
        _test(not version, "Tentative dataset should not have a version")
    else:
        _test(version, "No version")
        if record.get("version"):
            _test(
                re.match(r"v?\d+(\.\d+)*", record.get("version")),
                f"Invalid version: {record.get('version')}",
            )

    # DOI
    dois = [
        item
        for item in record.get("unique-resource-identifier-full", [])
        if "doi.org" in item.get("code", "")
    ]
    if not is_tentative:
        _test(dois, "No DOI defined")
    if dois:
        _test(
            len(dois) < 2,
            f"Multiple doi={dois}?",
        )
        _test(
            all(re.match("https://doi.org", doi.get("code", "")) for doi in dois),
            f"Some dois do not match the expected format {DOI_CODE_FORMAT}: doi={[doi.get('code') for doi in dois]}",
        )
        related_work_dois = {
            a.get("aggregate-dataset-identifier_code", "")
            for a in record.get("aggregation-info", [])
        }
        for doi in dois:
            response = requests.get(doi.get("code"), allow_redirects=True)
            _test(
                response.status_code in (200, 201, 403, 418, 503),
                f"Record DOI HTTPS link is failling: {doi.get('code')} status_code={response.status_code}",
            )
            if doi.get("code") not in related_work_dois:
                _test(
                    response.url.startswith("https://catalogue.hakai.org")
                    or response.url.startswith("https://doi.org"),
                    f"DOI is not redirecting to Hakai's catalogue: {response.url}",
                )

    # Related Works — flag malformed DOI URLs (https://10.x instead of https://doi.org/10.x)
    related_work_github_repos = set()
    related_work_codes = set()
    for agg in record.get("aggregation-info", []):
        code = agg.get("aggregate-dataset-identifier_code", "")
        _test(
            not re.match(r"https?://10\.", code, re.IGNORECASE),
            f"Malformed related work identifier (missing doi.org): {code}",
        )
        if code:
            related_work_codes.add(code.rstrip("/").lower())
        agg_owner_repo = _github_owner_repo(GITHUB_REPO_URL_RE.match(code))
        if agg_owner_repo:
            related_work_github_repos.add(agg_owner_repo)

    # Contacts
    contacts = record.get("cited-responsible-party", []) + record.get(
        "metadata-point-of-contact", []
    )

    # Funder
    funders = [item for item in contacts if "funder" in item["role"]]
    _test(funders, "No funder")
    for funder in funders:
        _test(
            funder.get("individual-name") or funder.get("organisation-name"),
            "Funder contact is missing a name or organisation",
        )

    # Publisher
    publishers = [contact for contact in contacts if "publisher" in contact["role"]]
    _test(publishers, "No publisher")
    for publisher in publishers:
        _test(
            publisher.get("individual-name") or publisher.get("organisation-name"),
            "Publisher contact is missing a name or organisation",
        )

    # Determine whether the record has been published for 6+ months
    pub_date_str = _date_by_type(record.get("metadata-reference-date", []), "publication")
    dataset_dates = record.get("dataset-reference-date", [])
    data_revision_date_str = _date_by_type(dataset_dates, "revision")
    data_publication_date_str = _date_by_type(dataset_dates, "publication")
    reference_date_str = data_revision_date_str or data_publication_date_str
    reference_date_label = "revision" if data_revision_date_str else "publication"
    reference_date = None
    if reference_date_str:
        try:
            reference_date = date.fromisoformat(reference_date_str)
        except ValueError:
            pass
    reference_years = set()
    for date_str in (data_revision_date_str, data_publication_date_str):
        if date_str:
            try:
                reference_years.add(date.fromisoformat(date_str).year)
            except ValueError:
                pass
    published_over_6_months = True
    if pub_date_str:
        try:
            pub = date.fromisoformat(pub_date_str)
            today = date.today()
            six_months_ago = today.replace(
                year=today.year if today.month > 6 else today.year - 1,
                month=today.month - 6 if today.month > 6 else today.month + 6,
            )
            published_over_6_months = pub <= six_months_ago
        except ValueError:
            pass

    # Resources
    for index, resource in enumerate(record.get("resources", [])):
        _test(resource["name"] != "", "Empty resource name")
        _test(resource["url"] != "", "Empty resource url")
        _test(resource["format"] != "", "Empty resource format")
        github_match = GITHUB_REPO_URL_RE.match(resource["url"])
        owner_repo = _github_owner_repo(github_match)
        is_github_repo_url = bool(github_match)
        is_related_work_url = resource["url"].rstrip("/").lower() in related_work_codes
        if owner_repo:
            is_related_work_url = is_related_work_url or owner_repo in related_work_github_repos
        _test(
            not is_related_work_url,
            f"Resource is also listed as a Related Work: {resource['url']}",
        )
        try:
            status_code = int(requests.get(resource["url"]).status_code)
        except requests.exceptions.Timeout:
            status_code = "timeout"
        accepted = {200, 201, 401, 403, 418, 503}
        if (not published_over_6_months) and is_github_repo_url:
            accepted.add(404)
        _test(
            status_code in accepted,
            f"Invalid Resource URL: {resource['url']} returned status_code={status_code}",
        )
        if is_github_repo_url:
            is_hakai_org_repo = resource["url"].startswith("https://github.com/HakaiInstitute/")
            _test(
                is_hakai_org_repo,
                f"Resource GitHub repository is not under the HakaiInstitute organization: {resource['url']}",
            )
            if is_hakai_org_repo and reference_date and not is_related_work_url:
                release_date = _get_latest_github_release_date(*owner_repo)
                if release_date is not None:
                    _test(
                        release_date.year == reference_date.year,
                        f"GitHub release date ({release_date.isoformat()}) is not in the same year as the "
                        f"data reference date ({reference_date_label}: {reference_date.isoformat()}): {resource['url']}",
                    )

        erddap_match = ERDDAP_RESOURCE_URL_RE.match(resource["url"])
        if erddap_match and not is_tentative:
            last_data_date = _get_erddap_last_data_date(*erddap_match.groups())
            if last_data_date is not None:
                _test(
                    bool(reference_years),
                    f"ERDDAP dataset has data through {last_data_date.isoformat()} but the record has no "
                    f"Data Reference Date (Publication or Revision): {resource['url']}",
                )
                if reference_years:
                    _test(
                        last_data_date.year <= max(reference_years),
                        f"ERDDAP last data point year ({last_data_date.year}) is later than the metadata "
                        f"Data Reference Date year(s) ({sorted(reference_years)}): {resource['url']}",
                    )

    # Spatial
    _test("spatial" in record, "No spatial information available")

    return results


def _should_skip_url(url: str) -> bool:
    return any(url.startswith(prefix) for prefix in _SKIP_URL_PREFIXES)


_URL_RE = re.compile(r"https?://[^\s<>\"')\]]+")


def _extract_record_links(record) -> set:
    """Collect all URLs from aggregation-info, lineage, and abstract fields."""
    urls = set()

    def _scan_text(text):
        for match in _URL_RE.findall(text or ""):
            urls.add(match.rstrip(".,;:!?)"))

    _scan_text(record.get("notes") or "")
    for text in (record.get("notes_translated") or {}).values():
        _scan_text(text)

    for agg in record.get("aggregation-info", []):
        code = agg.get("aggregate-dataset-identifier_code", "")
        if code and code.startswith("http"):
            urls.add(code)
    for entry in record.get("lineage", []):
        for step_str in entry.get("processing-step", []):
            try:
                step = json.loads(step_str) if isinstance(step_str, str) else step_str
                url = step.get("reference", {}).get("onlineResource", {}).get("url", "")
                if url:
                    urls.add(url)
            except Exception:
                pass
        for doc_str in entry.get("additional-documentation", []):
            try:
                doc = json.loads(doc_str) if isinstance(doc_str, str) else doc_str
                url = doc.get("onlineResource", {}).get("url", "")
                if url:
                    urls.add(url)
            except Exception:
                pass
        for src_str in entry.get("source", []):
            try:
                src = json.loads(src_str) if isinstance(src_str, str) else src_str
                url = src.get("citation", {}).get("onlineResource", {}).get("url", "")
                if url:
                    urls.add(url)
            except Exception:
                pass
    return urls


@logger.catch(default=[])
def check_record_links(record) -> list:
    """Check URLs in aggregation-info, lineage, and abstract fields for broken links.

    Flags HTTP error responses (4xx/5xx) but ignores timeouts, redirects, and
    auth-gated responses. Skips standards/vocabulary URLs (same exclusions as
    the lychee link checker).
    """
    results = []
    # 401/403 mean auth-required (resource exists), 418/503 are transient/intentional
    ok_statuses = {200, 201, 301, 302, 307, 308, 401, 403, 418, 503}
    for url in _extract_record_links(record):
        if _should_skip_url(url):
            continue
        try:
            response = requests.get(
                url,
                allow_redirects=True,
                timeout=15,
                headers={"User-Agent": "hakai-ckan-records-checks/link-checker"},
            )
            if response.status_code not in ok_statuses:
                results.append([f"Broken link ({response.status_code}): {url}"])
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.RequestException:
            results.append([f"Broken link (connection error): {url}"])
    return results


@logger.catch(default={})
def get_record_summary(record):
    dois = [
        item["code"]
        for item in record.get("unique-resource-identifier-full", [])
        if "doi.org" in item["code"]
    ]
    doi = dois[0].replace("https://doi.org/", "") if dois else ""
    maintenance_note = record.get("maintenance-note") or ""
    form_url = (
        maintenance_note.split("Generated from ")[-1].strip()
        if "Generated from" in maintenance_note
        else ""
    )
    metadata_dates = {
        f"metadata_{item['type']}": item["value"]
        for item in record.get("metadata-reference-date", [])
    }

    return {
        "id": record["id"],
        "name": record["name"],
        "organization": record["organization"]["title"],
        "title": record["title"],
        "resource-type": record.get("resource-type"),
        "licence": record.get("license_id"),
        "private": record.get("private"),
        "projects": ", ".join(record.get("projects", [])),
        "progress": record.get("progress"),
        "state": record.get("state"),
        "type": record.get("type"),
        "distributor": record.get("distributor", [{}])[0].get("organisation-name"),
        "resources_count": len(record.get("resources", [])),
        "spatial": record.get("spatial"),
        "vertical-extent": record.get("vertical-extent"),
        "eov": ", ".join(record.get("eov", [])),
        "doi": doi,
        "form_url": form_url,
        **metadata_dates,
    }
