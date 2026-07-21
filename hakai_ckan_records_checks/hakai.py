import difflib
import json
import re
from datetime import date

import pandas as pd
import requests
from loguru import logger

ORGANIZATIONS = [
    "Hakai Institute",
]
DOI_CODE_FORMAT = r"https\:\/\/doi\.org"

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
    for agg in record.get("aggregation-info", []):
        code = agg.get("aggregate-dataset-identifier_code", "")
        _test(
            not re.match(r"https?://10\.", code, re.IGNORECASE),
            f"Malformed related work identifier (missing doi.org): {code}",
        )

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
    pub_date_str = next(
        (d["value"] for d in record.get("metadata-reference-date", []) if d.get("type") == "publication"),
        None,
    )
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
        try:
            status_code = int(requests.get(resource["url"]).status_code)
        except requests.exceptions.Timeout:
            status_code = "timeout"
        accepted = {200, 201, 401, 403, 418, 503}
        is_github_repo_url = bool(re.match(r"^https?://github\.com/[^/]+/[^/]+/?$", resource["url"]))
        if (not published_over_6_months) and is_github_repo_url:
            accepted.add(404)
        _test(
            status_code in accepted,
            f"Invalid Resource URL: {resource['url']} returned status_code={status_code}",
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
