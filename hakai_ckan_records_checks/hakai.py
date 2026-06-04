import difflib
import json
import re

import pandas as pd
import requests
from loguru import logger

ORGANIZATIONS = [
    "Hakai Institute",
]
DOI_CODE_FORMAT = r"https\:\/\/doi\.org"


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
        for doi in dois:
            response = requests.get(doi.get("code"), allow_redirects=True)
            _test(
                response.status_code in (200, 201, 403, 418, 503),
                f"Record DOI HTTPS link is failling: {doi.get('code')} status_code={response.status_code}",
            )
            _test(
                response.url.startswith("https://catalogue.hakai.org")
                or response.url.startswith("https://doi.org"),
                f"DOI is not redirecting to Hakai's catalogue: {response.url}",
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

    # Resources
    for index, resource in enumerate(record.get("resources", [])):
        _test(resource["name"] != "", "Empty resource name")
        _test(resource["url"] != "", "Empty resource url")
        _test(resource["format"] != "", "Empty resource format")
        try:
            status_code = int(requests.get(resource["url"]).status_code)
        except requests.exceptions.Timeout:
            status_code = "timeout"
        _test(
            status_code in (200, 201, 401, 403, 418, 503),
            f"Invalid Resource URL: {resource['url']} returned status_code={status_code}",
        )

    # Spatial
    _test("spatial" in record, "No spatial information available")

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
