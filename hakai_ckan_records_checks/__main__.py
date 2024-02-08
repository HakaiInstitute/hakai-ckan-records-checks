import sys

import click
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from loguru import logger
from tqdm import tqdm

from hakai_ckan_records_checks import hakai
from hakai_ckan_records_checks.ckan import CKAN

environment = Environment(loader=FileSystemLoader("templates"))


def review_records(ckan: CKAN) -> dict:
    @logger.catch(default={})
    def _review_record(record_id) -> dict:
        record = ckan.get_record(record_id)
        assert record["success"] == True
        return {
            "record_id": record_id,
            "test_results": hakai.test_record_requirements(record["result"]),
            "summary": hakai.get_record_summary(record["result"]),
        }

    records = ckan.get_all_records()
    logger.info(f"Found {len(records['result'])} records in CKAN instance")
    results = []
    for record_id in tqdm(
        records["result"], desc=f"Checking {ckan.base_url} records", unit="records"
    ):
        results += [_review_record(record_id)]

    test_result_summary = pd.concat(
        [result["test_results"] for result in results if result]
    )
    catalog_summary = pd.concat([result["summary"] for result in results if result])

    return {
        "ckan_url": ckan.base_url,
        "summary": catalog_summary,
        "test_results": test_result_summary,
    }


@click.command()
@click.option("-c", "--ckan_url", help="The base URL of the CKAN instance")
@click.option("--api_key", default=None, help="The API key for the CKAN instance")
@click.option(
    "--output",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    default="output",
    help="directory where to save the output",
)
@click.option("--log_level", default="INFO", help="The log level for the application")
def main(ckan_url, api_key, output, log_level):
    logger.remove()
    logger.add(sys.stderr, level=log_level)

    logger.info("Starting checks for CKAN instance at {ckan_url}")
    ckan = CKAN(ckan_url, api_key)

    logger.info("Reviewing records")
    results = review_records(ckan)

    if not output:
        return

    environment.get_template("index.html").stream(**results).dump(f"{output}/home.md")


if __name__ == "__main__":
    main()
