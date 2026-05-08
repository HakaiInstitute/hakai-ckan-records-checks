import json
import re

import pandas as pd
import requests
from loguru import logger

ORGANIZATIONS = [
    "Hakai Institute",
]
DOI_CODE_FORMAT = r"https\:\/\/doi\.org"


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
    _test("license_id" in record, "No licence")
    _test(record.get("license_id") != "", "Empty licence")
    _test(
        record.get("license_id") == "CC-BY-4.0",
        f"Invalid licence: {record.get('license_id')}",
    )

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

    # ORCID and ROR
    for contact in contacts:
        _test(
            contact.get("individual-name") in (None, "")
            or (
                contact.get("individual-name")
                and "orcid.org" in contact.get("individual-uri_code", "")
            ),
            f"Contact missing ORCID: {contact['individual-name']=} {contact.get('organisation-name')=}",
        )
        _test(
            contact.get("organisation-name") in (None, "")
            or (
                contact.get("organisation-name")
                and "ror.org" in contact.get("organisation-uri_code", "")
            ),
            f"Contact missing organization ROR:  {contact['individual-name']=} {contact['organisation-name']=}",
        )

    # Resources
    for index, resource in enumerate(record.get("resources", [])):
        _test(resource["name"] != "", "Empty resource name")
        _test(resource["url"] != "", "Empty resource url")
        _test(resource["format"] != "", "Empty resource format")
        _test(
            resource["format"] in ["HTML", "ERDDAP", "OBIS", "PDF", "ZIP"],
            f"Invalid resource format: resources[{index}].format={resource['format']}",
        )
        try:
            status_code = int(requests.get(resource["url"]).status_code)
        except requests.exceptions.Timeout:
            status_code = "timeout"
        _test(
            status_code in (200, 201, 403, 418, 503),
            f"Invalid resources.url.status_code: {status_code} for resources[{index}].url={resource['url']}",
        )

    # Data access via standardized repositories
    _test(
        any(
            re.findall("obis|erddap|arcgis|ncei", resource["url"], re.IGNORECASE)
            for resource in record.get("resources", [])
        ),
        "Record isn't accesible via a standard data repository",
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
