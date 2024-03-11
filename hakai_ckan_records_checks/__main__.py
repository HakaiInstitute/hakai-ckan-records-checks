import pickle
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import click
import pandas as pd
import plotly.express as px
from jinja2 import Environment, FileSystemLoader
from loguru import logger
from tqdm import tqdm

from hakai_ckan_records_checks import hakai
from hakai_ckan_records_checks.ckan import CKAN

environment = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))
CACHE_FILE = Path("cache.pkl")
pd.set_option("future.no_silent_downcasting", True)
IGNORE_RECORD_IDS= (
    "hakai-metadata-form-data"
)

def format_summary(summary):
    def link_issue_page(record_row,var):
        if pd.isna(record_row[var]):
            return ""
        return f"<a title='{record_row['id']}' href='issues/{record_row['id']}.html' target='_blank'>{record_row[var]}</a>"

    def link_record_page_title(record_row,var='Catalogue Page'):
        if pd.isna(record_row["name"]):
            return ""
        return f"<a href='https://catalogue.hakai.org/dataset/{record_row['name']}' target='_blank'>{record_row[var]}</a>"

    summary = summary.dropna(subset=["id", "name", "organization", "title"], how="any")
    summary = summary.assign(
        WARNING=summary.apply(lambda x: link_issue_page(x,'WARNING'), axis=1),
        ERROR=summary.apply(lambda x: link_issue_page(x,'ERROR'), axis=1),
        title=summary.apply(lambda x: link_record_page_title(x, 'title'), axis=1),
    )
    return summary.astype({"resources_count": "int32"}).fillna("")


def review_records(ckan: str, max_workers, records_ids: list = None) -> dict:
    @logger.catch(default={})
    def _review_record(record_id) -> dict:
        record = ckan.get_record(record_id)
        assert record["success"] == True
        test_results = hakai.test_record_requirements(record["result"])
        summary = hakai.get_record_summary(record["result"])
        if not test_results.empty:
            summary.update(test_results.groupby("level").count()["record_id"].to_dict())

        return {
            "record_id": record_id,
            "test_results": test_results,
            "summary": summary,
        }

    if not records_ids:
        records = ckan.get_all_records()
    else:
        records = {"result": records_ids}

    logger.info(f"Found {len(records['result'])} records in CKAN instance")
    results = []
    with tqdm(
        total=len(records["result"]), desc="Checking records", unit="records"
    ) as pbar:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [
                executor.submit(_review_record, record_id)
                for record_id in records["result"]
                if record_id not in IGNORE_RECORD_IDS
            ]
            for future in as_completed(futures):
                results.append(future.result())
                pbar.update(1)

    test_result_summary = pd.concat(
        [result["test_results"] for result in results if result]
    )
    catalog_summary = pd.DataFrame([result["summary"] for result in results if result])

    return {
        "ckan_url": ckan.base_url,
        "catalog_summary": catalog_summary,
        "test_results": test_result_summary,
    }


@click.command()
@click.option("-c", "--ckan_url", help="The base URL of the CKAN instance")
@click.option("--record_ids", default=None, type=str, help="The records to check")
@click.option("--api_key", default=None, help="The API key for the CKAN instance")
@click.option(
    "--output",
    type=click.Path(file_okay=False, dir_okay=True),
    default="output",
    help="directory where to save the output",
)
@click.option("--max_workers", default=10, help="The maximum number of workers to use")
@click.option("--log_level", default="INFO", help="The log level for the application")
@click.option(
    "--cache/--no-cache", is_flag=True, default=True, help="Use cache if available"
)
def main(ckan_url, record_ids, api_key, output, max_workers, log_level, cache):
    logger.remove()
    logger.add(sys.stderr, level=log_level)

    logger.info("Starting checks for CKAN instance at {ckan_url}")
    ckan = CKAN(ckan_url, api_key)
    if record_ids:
        record_ids = record_ids.split(",")

    logger.info("Reviewing records")
    if cache and CACHE_FILE.exists():
        with open(CACHE_FILE, "rb") as file:
            logger.info("Loading cached results")
            results = pickle.load(file)
    else:
        results = review_records(ckan, max_workers, record_ids)

        with open(CACHE_FILE, "wb") as file:
            logger.info("Caching results")
            pickle.dump(results, file)

    if not output:
        return

    logger.info(f"Generate figures")
    # Combine summary and issues
    combined_issues = (
        results["test_results"]
        .merge(results["catalog_summary"], left_on="record_id", right_on="id")
        .drop(columns=["id"])
    )
    standardized_issues = combined_issues.copy()
    standardized_issues["message"] = standardized_issues["message"].str.replace(
        "resources\[[0-9]+\]", "resources[...]", regex=True
    )

    # Generate figures
    pie_chart = px.pie(
        standardized_issues,
        names="message",
        title=f"Hakai Records Issues Distribution: {len(standardized_issues)} issues detected",
        facet_col="level",
    )
    pie_chart.update_traces(textposition="inside")
    pie_chart.update_layout(uniformtext_minsize=12, uniformtext_mode="hide")
    pie_chart_html = pie_chart.to_html(full_html=False)

    # save results
    logger.info(f"Saving results to: {output=}")
    Path(output).mkdir(parents=True, exist_ok=True)
    environment.get_template("index.html.jinja").stream(
        catalog_summary=format_summary(results["catalog_summary"]),
        issues_pie_chart=pie_chart_html,
        issues_table=combined_issues,
        time=pd.Timestamp.utcnow(),
        ckan_url=ckan_url,
    ).dump(f"{output}/index.html")
    # create record specific pages
    catalog_summary = results["catalog_summary"].set_index("id")
    Path(output, "issues").mkdir(parents=True, exist_ok=True)
    for record_id, issues in results["test_results"].groupby("record_id"):
        environment.get_template("record.html.jinja").stream(
            record=catalog_summary.loc[record_id],
            issues=issues,
            time=pd.Timestamp.utcnow(),
        ).dump(f"{output}/issues/{record_id}.html")

    logger.info("Save excel and csv outputs")
    results["catalog_summary"].to_excel(f"{output}/catalog_summary.xlsx", index=True)
    results["catalog_summary"].to_csv(f"{output}/catalog_summary.csv", index=True)
    results["test_results"].to_csv(f"{output}/issues_list.csv", index=True)
    results["test_results"].to_excel(f"{output}/issues_list.xlsx", index=True)


if __name__ == "__main__":
    main()
