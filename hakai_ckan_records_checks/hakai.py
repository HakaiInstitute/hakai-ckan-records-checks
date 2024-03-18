import json
import re

import pandas as pd
import requests
from loguru import logger

ORGANIZATIONS = [
    "Hakai Institute",
]


def test(condition, level, message):
    if not condition:
        logger.log(level, message)
        raise Exception(message)
    if not condition:
        logger.log(level, message)


@logger.catch(default=pd.DataFrame())
def test_record_requirements(record) -> pd.DataFrame:
    """Run a series of tests on a record to ensure it meets Hakai's metadata requirements"""

    def _test(condition, level, message):
        if not condition:
            logger.log(level, message)
            results.append([level, message])

    results = []
    logger.debug("Review Record {}", record["id"])

    # organization
    _test("organization" in record, "ERROR", "No organization")
    _test(
        record["organization"]["title"] in ORGANIZATIONS,
        "ERROR",
        f"Unknown organization title: {record['organization']['title']}",
    )
    _test(record.get("projects"), "ERROR", "No projects associated")
    _test(
        [
            uri
            for uri in record["organization"]["organization-uri"]
            if uri["authority"] == "ROR"
        ],
        "WARNING",
        "Organization is missing an ROR URI",
    )

    # review title
    _test(record.get("title") != "", "ERROR", "No title")
    _test(
        not re.findall(r"[A-Z\.]{3,}", record.get("title", "")),
        "WARNING",
        "Title contains acronyms potentially",
    )
    _test(
        not re.match(r"v\d+|version", record.get("title", ""), re.IGNORECASE),
        "WARNING",
        "Title contains versioning information",
    )
    _test(
        not re.match(r"dataset", record.get("title", ""), re.IGNORECASE),
        "INFO",
        "Title contains the word dataset",
    )
    _test(
        len(record.get("title", "")) < 60, "INFO", "Title is greater than 60 characters"
    )

    # Review licence
    _test("license_id" in record, "ERROR", "No licence")
    _test(record.get("license_id") != "", "ERROR", "Empty licence")
    _test(
        record.get("license_id") == "CC-BY-4.0",
        "ERROR",
        f"Invalid licence: {record.get('license_id') }",
    )

    citation = json.loads(record["citation"]["en"].replace('\\"', '"'))
    # Review version
    version = citation[0].get("version")
    _test(version, "INFO", "No version")
    if record.get("version"):
        _test(
            re.match(r"v?\d+(\.\d+)*", record.get("version")),
            "ERROR",
            f"Invalid version: {record.get('version')}",
        )

    # Review identifier
    dois = [
        item
        for item in record.get("unique-resource-identifier-full", [])
        if "doi.org" in item.get("code", "")
    ]
    _test(
        dois,
        "WARNING",
        f"No DOI defined",
    )
    if dois:
        _test(
            len(dois) < 2,
            "ERROR",
            f"Multiple doi={dois}?",
        )
        DOI_CODE_FORMAT = r"https\:\/\/doi\.org"
        _test(
            all([re.match("https://doi.org", doi.get("code", "")) for doi in dois]),
            "ERROR",
            f"Some dois do not match the expected format {DOI_CODE_FORMAT}: doi={[doi.get('code') for doi in dois]}",
        )
        for doi in dois:
            _test(
                re.match("https://doi.org", doi.get("code", "")),
                "ERROR",
                f"Some dois do not match the exected format{DOI_CODE_FORMAT}: doi={doi.get('code')}",
            )
            status_code = requests.get(doi.get("code")).status_code
            _test(
                status_code in (200, 201, 403, 418, 503),
                "ERROR",
                f"Record DOI HTTPS link is failling: {doi.get('code')} status_code={status_code}",
            )

    # Review distributor
    _test("distributor" in record, "ERROR", "No distributor")
    _test(record.get("distributor") != "", "ERROR", "Empty distributor")
    organization_name = record.get("distributor", [{}])[0].get("organisation-name")
    _test(
        "Hakai" in organization_name and organization_name == "Hakai Institute",
        "ERROR",
        f"Invalid distributor organisation-name: {organization_name=} expects 'Hakai Institute'",
    )

    # Contacts related checks
    contacts = record.get("cited-responsible-party", []) + record.get(
        "metadata-point-of-contact", []
    )

    # Review funder
    funders = [item for item in contacts if "funder" in item["role"]]
    _test(len(funders) > 0, "WARNING", "No funder")
    if funders:
        _test(
            [
                funder.get("organisation-name") == "Hakai Institute"
                for funder in funders
            ],
            "WARNING",
            f"'Hakai Institute' isn't listed as funder in record",
        )

    # Review publisher
    publishers = [contact for contact in contacts if "publisher" in contact["role"]]
    _test(len(publishers) > 0, "WARNING", "No publisher")

    # Review contacts
    for contact in contacts:
        is_hakai_contact = "@hakai.org" in contact.get(
            "organisation-info_email", ""
        ) or "Hakai Institute" in contact.get("organisation-name", "")
        _test(
            contact.get("individual-name") in (None, "")
            or (
                contact.get("individual-name")
                and "orcid.org" in contact.get("individual-uri_code", "")
            ),
            "WARNING" if is_hakai_contact else "INFO",
            f"Contact missing ORCID: {contact['individual-name']=} {contact.get('organisation-name')=}",
        )
        _test(
            contact.get("organisation-name") in (None, "")
            or (
                contact.get("organisation-name")
                and "ror.org" in contact.get("organisation-uri_code", "")
            ),
            "WARNING" if is_hakai_contact else "INFO",
            f"Contact missing organization ROR:  {contact['individual-name']=} {contact['organisation-name']=}",
        )

    # Review resources
    for index, resource in enumerate(record.get("resources", [])):
        _test(resource["name"] != "", "ERROR", "Empty resource name")
        _test(resource["url"] != "", "ERROR", "Empty resource url")
        _test(resource["format"] != "", "ERROR", "Empty resource format")
        _test(
            resource["format"] in ["HTML", "ERDDAP", "OBIS", "PDF", "ZIP"],
            "ERROR",
            f"Invalid resource format: resources[{index}].format={resource['format']}",
        )
        try:
            status_code = int(requests.get(resource["url"]).status_code)
        except requests.exceptions.Timeout:
            status_code = "timeout"
        _test(
            status_code in (200, 201, 403, 418, 503),
            "ERROR",
            f"Invalid resources.url.status_code: {status_code} for resources[{index}].url={resource['url']}",
        )

    # Data Access via Standardized Repositories
    _test(
        any(
            [
                re.findall("obis|erddap|arcgis|ncei", resource["url"], re.IGNORECASE)
                for resource in record.get("resources", [])
            ]
        ),
        "INFO",
        "Record isn't accesible via a standard data repository",
    )

    # test spatial
    _test("spatial" in record, "ERROR", "No spatial information available")

    summary = pd.DataFrame(results, columns=["level", "message"])
    summary.insert(0, "record_id", record["id"])
    return summary


@logger.catch(default={})
def get_record_summary(record):
    return {
        "id": record["id"],
        "name": record["name"],
        "organization": record["organization"]["title"],
        "title": record["title"],
        "ressource-type": record.get("resource-type"),
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
        "metadata_created": record.get("metadata_created"),
        "metadata_modified": record.get("metadata_modified"),
    }
