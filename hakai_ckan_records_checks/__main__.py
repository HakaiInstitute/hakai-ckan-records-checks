import base64
import datetime
import json
import os
import pickle
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import click
import numpy as np
import pandas as pd
import plotly.express as px
from jinja2 import Environment, FileSystemLoader
from loguru import logger
from tqdm import tqdm

from hakai_ckan_records_checks import hakai
from hakai_ckan_records_checks.ckan import CKAN
from hakai_ckan_records_checks.datacite import Datacite, get_datacite_summary

REPO_URL = os.getenv(
    "REPO_URL", "https://github.com/HakaiInstitute/hakai-ckan-records-checks"
)

environment = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))
CACHE_FILE = Path("cache.pkl")
pd.set_option("future.no_silent_downcasting", True)
IGNORE_RECORD_IDS = "hakai-metadata-form-data"
level_type = pd.CategoricalDtype(categories=["INFO", "WARNING", "ERROR"], ordered=True)


def fig_to_json(fig):
    def to_serializable(obj):
        if isinstance(obj, dict):
            if "bdata" in obj and "dtype" in obj:
                return np.frombuffer(base64.b64decode(obj["bdata"]), dtype=np.dtype("<" + obj["dtype"])).tolist()
            return {k: to_serializable(v) for k, v in obj.items()}
        if isinstance(obj, (list, tuple)):
            return [to_serializable(v) for v in obj]
        if isinstance(obj, np.ndarray):
            return [to_serializable(v) for v in obj.tolist()]
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        return obj
    return json.dumps(to_serializable(fig.to_dict()))


def format_summary(summary, base_url=""):
    def link_issue_page(record_row, var):
        if pd.isna(record_row[var]):
            return ""
        return f"<a title='{record_row['id']}' href='{base_url}records/{record_row['id']}' target='_blank'>{record_row[var]}</a>"

    for col in ["INFO", "WARNING", "ERROR", "sum"]:
        if col not in summary.columns:
            summary[col] = pd.NA
    summary[["INFO", "WARNING", "ERROR", "sum"]] = summary[
        ["INFO", "WARNING", "ERROR", "sum"]
    ].astype("Int64")
    summary = summary.dropna(subset=["id", "name", "organization", "title"], how="any")
    summary = summary.assign(
        INFO=summary.apply(lambda x: link_issue_page(x, "INFO"), axis=1),
        WARNING=summary.apply(lambda x: link_issue_page(x, "WARNING"), axis=1),
        ERROR=summary.apply(lambda x: link_issue_page(x, "ERROR"), axis=1),
        sum=summary.apply(lambda x: link_issue_page(x, "sum"), axis=1),
        Title="<a href='https://catalogue.hakai.org/dataset/"
        + summary["name"]
        + "' target='_blank'>"
        + summary["title"].fillna("")
        + "</a>",
    )
    if "citation_count" not in summary.columns:
        summary["citation_count"] = pd.NA
    summary["citation_count"] = summary["citation_count"].fillna(-1)
    summary["Last Revised"] = summary["metadata_revision"].fillna(summary["metadata_publication"])

    return summary.astype(
        {"resources_count": "int32", "citation_count": "int32"}
    ).fillna("")


def compute_metrics(catalog_summary):
    total = len(catalog_summary)
    with_doi = int((catalog_summary["doi"].fillna("") != "").sum())
    with_issues = int(catalog_summary["sum"].notna().sum()) if "sum" in catalog_summary.columns else 0
    total_errors = int(catalog_summary["ERROR"].fillna(0).sum()) if "ERROR" in catalog_summary.columns else 0
    total_warnings = int(catalog_summary["WARNING"].fillna(0).sum()) if "WARNING" in catalog_summary.columns else 0
    return {
        "date": pd.Timestamp.now().date().isoformat(),
        "total_records": total,
        "records_with_issues": with_issues,
        "pct_with_doi": round(with_doi / total * 100, 1) if total > 0 else 0.0,
        "total_errors": total_errors,
        "total_warnings": total_warnings,
    }


def _build_metric(label, value_str, raw_delta, lower_is_better=None, pct=False, previous_date=None):
    delta_str = None
    color = "gray"
    if raw_delta is not None and raw_delta != 0:
        sign = "+" if raw_delta > 0 else ""
        suffix = "%" if pct else ""
        delta_str = f"{sign}{raw_delta}{suffix}"
        if lower_is_better is not None:
            color = "green" if (raw_delta < 0) == lower_is_better else "red"
    return {"label": label, "value": value_str, "delta": delta_str, "color": color, "previous_date": previous_date}


def review_records(ckan: str, max_workers, records_ids: list = None) -> dict:
    @logger.catch(default={})
    def _review_record(record_id) -> dict:
        record = ckan.get_record(record_id)
        assert record["success"]
        test_results = hakai.test_record_requirements(record["result"])
        summary = hakai.get_record_summary(record["result"])

        logger.debug("Getting citation count for DOI")
        datacite_metadata, error_msg = Datacite().get_doi(summary.get("doi"))
        summary.update(get_datacite_summary(datacite_metadata))
        if error_msg:
            test_results.append(["ERROR", error_msg])
        test_results = pd.DataFrame(test_results, columns=["level", "message"])
        test_results.insert(0, "record_id", record["result"]["id"])

        if len(test_results) > 0:
            issues_count = (
                test_results.groupby("level").count()["record_id"].astype(int)
            )
            summary.update({**issues_count.to_dict(), "sum": issues_count.sum()})

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

    logger.info("Generate figures")
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
    grouped_issues = (
        standardized_issues
        .drop_duplicates(subset=["record_id", "message"])
        .groupby("message")
        .size()
        .sort_values()
        .reset_index(name="count")
    )

    figure_issues_distribution = px.bar(
        grouped_issues,
        x="count",
        y="message",
        text="count",
        labels={"count": "Number of Records with Issue"},
        orientation="h",
        template="none",
        color_discrete_sequence=["#AA2026"],
    )

    figure_issues_distribution.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(
            title="Number of Records with Issue",
            tickformat="d",
        ),
        yaxis=dict(
            tickfont=dict(size=10),
            linecolor="black",
            title=None,
            automargin=True,
        ),
        margin=dict(l=0, r=60, t=20, b=40),
        showlegend=False,
    )
    figure_issues_distribution.update_traces(textposition="outside", cliponaxis=False)

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
    citations_over_time = (
        pd.DataFrame(
            [
                {"title": title, "year": year["year"], "citations": year["total"]}
                for title, years in results["catalog_summary"]
                .set_index("title")["citations_over_time"]
                .dropna()
                .to_dict()
                .items()
                for year in years
            ]
        )
        .astype({"citations": int})
        .sort_values(["year", "title"])
    )
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
    
    logger.info(f"Saving results to: {output=}")
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)

    # Compute and persist metrics history
    current_metrics = compute_metrics(results["catalog_summary"])
    metrics_file = output / "metrics_history.json"
    history = json.loads(metrics_file.read_text()) if metrics_file.exists() else []
    previous = history[-1] if history else None
    delta = {}
    if previous:
        for k, v in current_metrics.items():
            if k != "date" and isinstance(v, (int, float)):
                d = round(v - previous.get(k, v), 1)
                delta[k] = d if d != 0 else None
    history.append(current_metrics)
    metrics_file.write_text(json.dumps(history[-52:], indent=2))

    prev_date = previous["date"] if previous else None
    metrics_display = [
        _build_metric("Total Records", str(current_metrics["total_records"]), delta.get("total_records"), previous_date=prev_date),
        _build_metric("Records with Issues", str(current_metrics["records_with_issues"]), delta.get("records_with_issues"), lower_is_better=True, previous_date=prev_date),
        _build_metric("% Records with DOI", f"{current_metrics['pct_with_doi']}%", delta.get("pct_with_doi"), lower_is_better=False, pct=True, previous_date=prev_date),
    ]

    figure_issues_distribution_json = fig_to_json(figure_issues_distribution)
    timeseries_figure_json = fig_to_json(timeseries_figure)
    citations_over_time_figure_json = fig_to_json(citations_over_time_figure)

    environment.get_template("index.md").stream(
        catalog_summary=format_summary(results["catalog_summary"]),
        timeseries_figure_json=timeseries_figure_json,
        citations_over_time_figure_json=citations_over_time_figure_json,
        figure_issues_distribution_json=figure_issues_distribution_json,
        ckan_url=ckan_url,
        metrics=metrics_display,
    ).dump(f"{output}/index.md")

    # save issue summary page
    Path(output, "issues").mkdir(parents=True, exist_ok=True)
    environment.get_template("issues.md").stream(
        catalog_summary=format_summary(results["catalog_summary"], base_url="../"),
        timeseries_figure_json=timeseries_figure_json,
        citations_over_time_figure_json=citations_over_time_figure_json,
        figure_issues_distribution_json=figure_issues_distribution_json,
        issues_table=combined_issues,
    ).dump(f"{output}/issues/index.md")

    # create an issue specifc page
    for issue, issues in grouped_issues.groupby("message"):
        filename = re.sub(r"[\.\'\"]", "", issue)
        filename = re.sub(r"[^a-zA-Z0-9]", "-", filename).lower()
        filename = re.sub(r"-+", "-", filename)

        environment.get_template("issue.md").stream(
            title=issue,
            issues_table=combined_issues.query("message.str.startswith(@issue)"),
        ).dump(f"{output}/issues/{filename}.md")

    # create record specific pages
    catalog_summary_for_html = format_summary(results["catalog_summary"], base_url="../").set_index("id")
    Path(output, "records").mkdir(parents=True, exist_ok=True)
    for record_id, issues in results["test_results"].groupby("record_id"):
        record = catalog_summary_for_html.loc[record_id]
        environment.get_template("record.md").stream(
            record=record,
            form_url=record.get("form_url", ""),
            issues=issues,
            pd=pd,
        ).dump(f"{output}/records/{record_id}.md")

    logger.info("Save excel and csv outputs")
    results["catalog_summary"].to_excel(f"{output}/catalog_summary.xlsx", index=True)
    results["catalog_summary"].to_csv(f"{output}/catalog_summary.csv", index=True)
    results["test_results"].to_csv(f"{output}/issues_list.csv", index=True)
    results["test_results"].to_excel(f"{output}/issues_list.xlsx", index=True)


if __name__ == "__main__":
    main()
