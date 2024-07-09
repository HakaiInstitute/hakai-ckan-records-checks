import os
import pickle
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import click
import pandas as pd
import plotly.express as px
import plotly.io as pio
from jinja2 import Environment, FileSystemLoader
from loguru import logger
from tqdm import tqdm

from hakai_ckan_records_checks import hakai
from hakai_ckan_records_checks.ckan import CKAN
from hakai_ckan_records_checks.datacite import Datacite

REPO_URL = os.getenv(
    "REPO_URL", "https://github.com/HakaiInstitute/hakai-ckan-records-checks"
)

environment = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))
CACHE_FILE = Path("cache.pkl")
pd.set_option("future.no_silent_downcasting", True)
IGNORE_RECORD_IDS = "hakai-metadata-form-data"
level_type = pd.CategoricalDtype(categories=["INFO", "WARNING", "ERROR"], ordered=True)


def format_summary(summary):
    def link_issue_page(record_row, var):
        if pd.isna(record_row[var]):
            return ""
        return f"<a title='{record_row['id']}' href='issues/{record_row['id']}' target='_blank'>{record_row[var]}</a>"

    summary[["INFO", "WARNING", "ERROR", "sum"]] = summary[
        ["INFO", "WARNING", "ERROR", "sum"]
    ].astype("Int64")
    summary = summary.dropna(subset=["id", "name", "organization", "title"], how="any")
    summary = summary.assign(
        INFO=summary.apply(lambda x: link_issue_page(x, "INFO"), axis=1),
        WARNING=summary.apply(lambda x: link_issue_page(x, "WARNING"), axis=1),
        ERROR=summary.apply(lambda x: link_issue_page(x, "ERROR"), axis=1),
        sum=summary.apply(lambda x: link_issue_page(x, "sum"), axis=1),
        Title=summary.apply(lambda x: link_issue_page(x, "title"), axis=1),
        Catalogue="<a href='https://catalogue.hakai.org/dataset/"
        + summary["name"]
        + "' target='_blank'>link</a>",
    )
    summary["citation_count"] = summary["citation_count"].fillna(-1)

    return summary.astype(
        {"resources_count": "int32", "citation_count": "int32"}
    ).fillna("")


def review_records(ckan: str, max_workers, records_ids: list = None) -> dict:
    @logger.catch(default={})
    def _review_record(record_id) -> dict:
        record = ckan.get_record(record_id)
        assert record["success"] == True
        test_results = hakai.test_record_requirements(record["result"])
        summary = hakai.get_record_summary(record["result"])
        if len(test_results) > 0:
            issues_count = (
                test_results.groupby("level").count()["record_id"].astype(int)
            )
            summary.update({**issues_count.to_dict(), "sum": issues_count.sum()})

        if summary["doi"]:
            logger.debug("Getting citation count for DOI")
            datacite = Datacite()
            doi_metadata = datacite.get_doi(summary["doi"])
            summary["citation_count"] = doi_metadata["data"]["attributes"][
                "citationCount"
            ]
            summary["citations_over_time"] = doi_metadata["data"]["attributes"][
                "citationsOverTime"
            ]
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
    catalog_summary = (
        pd.DataFrame([result["summary"] for result in results if result])
        .sort_values("metadata_publication")
        .reset_index(drop=True)
    )

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
    default="docs",
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
        .astype({"level": level_type})
    )
    standardized_issues = combined_issues.copy()
    standardized_issues["message"] = standardized_issues["message"].apply(
        lambda x: x.split(":")[0] if x else x
    )
    standardized_issues["level"] = standardized_issues["level"].astype(level_type)
    grouped_issues = (
        standardized_issues.groupby(["level", "message"])
        .count()["record_id"]
        .sort_index()
        .reset_index()
    )

    figure = px.histogram(
        grouped_issues,
        x="message",
        y="record_id",
        color="level",
        labels={"record_id": "Issue"},
        color_discrete_map={"INFO": "lightblue", "WARNING": "orange", "ERROR": "red"},
    )

    figure.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1,
            xanchor="left",
            x=0,
            font=dict(size=10),
            itemwidth=30,
        ),
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(
            tickfont=dict(
                size=10,
            ),
            linecolor="black",
            title=None,
        ),
    )
    figure.update_traces(textposition="inside")
    figure.update_layout(uniformtext_minsize=12, uniformtext_mode="hide")

    # submission timeseries
    publication_time = pd.to_datetime(
        results["catalog_summary"]["metadata_publication"]
    )
    submission_timeseries = pd.DataFrame(
        {"publication_time": publication_time, "value": 1}
    ).sort_values("publication_time")
    submission_timeseries["cumulative"] = submission_timeseries["value"].cumsum()
    timeseries_figure = px.area(
        submission_timeseries,
        x="publication_time",
        y="cumulative",
        labels={"cumulative": "Published Records", "publication_time": ""},
        color_discrete_sequence=["#AA2026"],
    )

    # citation count timeseries
    citations_over_time = pd.DataFrame(
        [
            {"title": title, "year": year["year"], "citations": year["total"]}
            for title, years in results["catalog_summary"]
            .set_index("title")["citations_over_time"]
            .dropna()
            .to_dict()
            .items()
            for year in years
        ]
    ).astype({"citations": int}).sort_values(['year','title'])
    citations_over_time_figure = px.bar(
        citations_over_time,
        x="year",
        y="citations",
        color="title",
        labels={"citations": "Citations", "year": "Year", "title": "Title"},
    )
    citations_over_time_figure.update_layout(
        showlegend=False,
    )
    # save results
    catalog_summary_for_html = format_summary(results["catalog_summary"])

    logger.info(f"Saving results to: {output=}")
    Path(output).mkdir(parents=True, exist_ok=True)
    environment.get_template("index.md").stream(
        catalog_summary=catalog_summary_for_html,
        timeseries_figure=timeseries_figure,
        citations_over_time_figure=citations_over_time_figure,
        figure=figure,
        pio=pio,
        issues_table=combined_issues,
        time=pd.Timestamp.utcnow(),
        ckan_url=ckan_url,
        generated_by=REPO_URL,
    ).dump(f"{output}/index.md")

    # create record specific pages
    catalog_summary_for_html = catalog_summary_for_html.set_index("id")
    Path(output, "issues").mkdir(parents=True, exist_ok=True)
    for record_id, issues in results["test_results"].groupby("record_id"):
        environment.get_template("record.md").stream(
            record=catalog_summary_for_html.loc[record_id],
            issues=issues,
            time=pd.Timestamp.utcnow(),
            generated_by=REPO_URL,
        ).dump(f"{output}/issues/{record_id}.md")

    logger.info("Save excel and csv outputs")
    results["catalog_summary"].to_excel(f"{output}/catalog_summary.xlsx", index=True)
    results["catalog_summary"].to_csv(f"{output}/catalog_summary.csv", index=True)
    results["test_results"].to_csv(f"{output}/issues_list.csv", index=True)
    results["test_results"].to_excel(f"{output}/issues_list.xlsx", index=True)


if __name__ == "__main__":
    main()
