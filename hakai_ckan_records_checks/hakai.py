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
    _test(record["organization"].get("projects"), "ERROR", "No projects associated")

    # Review licence
    _test("license_id" in record, "ERROR", "No licence")
    _test(record.get("license_id") != "", "ERROR", "Empty licence")
    _test(
        record.get("license_id") == "CC-BY-4.0",
        "ERROR",
        f"Invalid licence={record.get('license_id') }",
    )

    # Review identifier
    dois = [item for item in record.get("unique-resource-identifier-full", []) if "doi.org" in item.get("code", "")]
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
            f"Some dois do not match the exected format{DOI_CODE_FORMAT}: doi={[doi.get('code') for doi in dois]}",
        )
        for doi in dois:
            _test(
                re.match("https://doi.org", doi.get("code", "")),
                "ERROR",
                f"Some dois do not match the exected format{DOI_CODE_FORMAT}: doi={doi.get('code')}",
            )
            status_code = requests.get(doi.get("code")).status_code
            _test(
                status_code in (200, 201),
                "ERROR",
                f"Invalid HTTPS {doi.get('code')} status_code={status_code}",
            )

    # Review distributor
    _test("distributor" in record, "ERROR", "No distributor")
    _test(record.get("distributor") != "", "ERROR", "Empty distributor")
    organization_name = record.get("distributor", [{}])[0].get("organisation-name")
    _test(
        organization_name == "Hakai Institute",
        "ERROR",
        f"Invalid distributor organisation-name={organization_name}",
    )

    # Review funder
    funders = [
        item
        for item in record.get("cited-responsible-party", [])
        if "funder" in item["role"]
    ]
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
        _test(
            int(requests.get(resource["url"]).status_code) in (200, 201),
            "ERROR",
            f"Invalid resources[{index}].url.status_code={requests.get(resource['url']).status_code}",
        )

    # Data Access via Standardized Repositories
    _test(
        any(
            [
                re.match("obis|erddap|argis", resource["url"], re.IGNORECASE)
                for resource in record.get("resources", [])
            ]
        ),
        "WARNING",
        "Record isn't accesible via a general public repository",
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
    }
