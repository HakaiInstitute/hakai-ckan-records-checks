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
        "Invalid distributor organisation name",
    )

    # Review publisher

    # Review ressources
    for index, ressource in enumerate(record["resources"]):
        _test(ressource["name"] != "", "ERROR", "Empty ressource name")
        _test(ressource["url"] != "", "ERROR", "Empty ressource url")
        _test(ressource["format"] != "", "ERROR", "Empty ressource format")
        _test(
            ressource["format"] in ["HTML"],
            "ERROR",
            f"Invalid ressource format: resources[{index}].format={ressource['format']}",
        )
        _test(
            requests.get(ressource["url"]).status_code == 200,
            "ERROR",
            f"Invalid ressources[{index}].url.status_code={requests.get(ressource['url']).status_code}",
        )

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
        "projects": record["projects"],
        "progress": record["progress"],
        "state": record["state"],
        "type": record["type"],
        "distributor": record["distributor"][0]["organisation-name"],
        "resources_count": len(record["resources"]),
        "spatial": record["spatial"],
        "vertical-extent": record["vertical-extent"],
        "eov": record["eov"],
    }
