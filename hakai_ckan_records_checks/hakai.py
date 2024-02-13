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

    # Review licence
    _test("license_id" in record, "ERROR", "No licence")
    _test(record["license_id"] != "", "ERROR", "Empty licence")
    _test(
        record["license_id"] == "CC-BY-4.0",
        "ERROR",
        f"Invalid licence={record['license_id'] }",
    )

    # Review distributor
    _test("distributor" in record, "ERROR", "No distributor")
    _test(record["distributor"] != "", "ERROR", "Empty distributor")
    _test(
        record["distributor"][0]["organisation-name"] == "Hakai Institute",
        "ERROR",
        f"Invalid distributor organisation-name={record['distributor'][0]['organisation-name']}",
    )

    # Review funder
    funders = [
        item for item in record["cited-responsible-party"] if "funder" in item["role"]
    ]
    _test(len(funders) > 0, "WARNING", "No funder")
    if funders:
        _test(
            [funder["organisation-name"] == "Hakai Institute" for funder in funders],
            "WARNING",
            f"'Hakai Institute' isn't listed as funder in record",
        )

    # Review publisher

    # Review resources
    for index, resource in enumerate(record["resources"]):
        _test(resource["name"] != "", "ERROR", "Empty resource name")
        _test(resource["url"] != "", "ERROR", "Empty resource url")
        _test(resource["format"] != "", "ERROR", "Empty resource format")
        _test(
            resource["format"] in ["HTML", "ERDDAP", "OBIS"],
            "ERROR",
            f"Invalid resource format: resources[{index}].format={resource['format']}",
        )
        _test(
            int(requests.get(resource["url"]).status_code) in (200, 201),
            "ERROR",
            f"Invalid resources[{index}].url.status_code={requests.get(resource['url']).status_code}",
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
        "licence": record["license_id"],
        "private": record["private"],
        "projects": ", ".join(record["projects"]),
        "progress": record["progress"],
        "state": record["state"],
        "type": record["type"],
        "distributor": record["distributor"][0]["organisation-name"],
        "resources_count": len(record["resources"]),
        "spatial": record["spatial"],
        "vertical-extent": record["vertical-extent"],
        "eov": ", ".join(record["eov"]),
    }
