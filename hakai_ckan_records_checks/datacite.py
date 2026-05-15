import json
import re

import requests
from loguru import logger

from hakai_ckan_records_checks.hakai import _fuzzy_match

DATACITE_API_URL = "https://api.datacite.org/dois"

RELATIONSHIPS_TRACKED = [
    "references",
    "citations",
    "parts",
    "partOf",
    "versions",
    "versionOf",
]

# relationType values auto-populated by DataCite (not manually curated)
_SKIP_RELATION_TYPES = {"Cites", "IsCitedBy", "IsSupplementTo", "IsSupplementedBy"}



def _normalize_identifier(identifier, id_type=""):
    """Normalize a related identifier for comparison (lowercase, strip trailing slash, strip DOI prefix)."""
    if not identifier:
        return ""
    identifier = identifier.rstrip("/")
    if id_type.upper() == "DOI" or "doi.org" in identifier.lower():
        identifier = re.sub(
            r"https?://(dx\.)?doi\.org/", "", identifier, flags=re.IGNORECASE
        )
    return identifier.lower()


class Datacite:
    def __init__(self):
        self.url = DATACITE_API_URL

    @logger.catch(default={})
    def get_doi(self, doi: str):
        """Get metadata for a DOI from DataCite"""
        if not doi:
            return {}, None

        response = requests.get(f"{self.url}/{doi}")
        if response.status_code != 200:
            error = json.loads(response.text)["errors"][0]
            msg = f"Failed to retrieve DOI from dataCite [{error['status']}] {error['title']}: {doi}"
            logger.error(msg)
            return {}, msg
        return response.json(), None


def get_datacite_summary(record):
    def review_doi(doi):
        response = requests.get(f"https://doi.org/{doi}")
        return {"status_code": response.status_code, "url": response.url}

    if not record:
        return {}
    if record["data"]["attributes"]["citationCount"] > 0:
        logger.info(
            f"Found citation count: {record['data']['attributes']['citationCount']}"
        )

    # Generate relationships table
    if record["data"]["attributes"]["citationCount"]:
        relationships = [
            {"relationship": relationship, **item, **review_doi(item["id"])}
            for relationship, attrs in record["data"]["relationships"].items()
            if relationship in RELATIONSHIPS_TRACKED and attrs["data"]
            for item in attrs["data"]
        ]
    else:
        relationships = []
    if relationships:
        logger.debug(f"Found relationships: {relationships}")
    return {
        "citation_count": record["data"]["attributes"]["citationCount"],
        "citations_over_time": record["data"]["attributes"]["citationsOverTime"],
        "relationships": relationships,
    }


def compare_datacite_metadata(ckan_record, datacite_metadata):
    """Compare CKAN record metadata against DataCite metadata and return a list of issue messages."""
    if not datacite_metadata or "data" not in datacite_metadata:
        return []

    attrs = datacite_metadata["data"]["attributes"]
    issues = []

    try:
        ckan_citation = json.loads(
            (ckan_record.get("citation") or {}).get("en", "[]").replace('\\"', '"')
        )
        ckan_citation = ckan_citation[0] if ckan_citation else {}
    except Exception:
        ckan_citation = {}

    # Title
    dc_titles = attrs.get("titles", [])
    primary_dc_title = next(
        (t["title"] for t in dc_titles if not t.get("titleType")),
        dc_titles[0]["title"] if dc_titles else None,
    )
    if primary_dc_title:
        ckan_title = ckan_record.get("title", "")
        if not _fuzzy_match(ckan_title, primary_dc_title, threshold=0.80):
            issues.append(
                f"Metadata mismatch: title CKAN='{ckan_title}' | DataCite='{primary_dc_title}'"
            )

    # License
    dc_rights = attrs.get("rightsList", [])
    if dc_rights:
        dc_license = dc_rights[0].get("rightsIdentifier", "").upper()
        ckan_license = ckan_record.get("license_id", "").upper()
        if dc_license and ckan_license and dc_license != ckan_license:
            issues.append(
                f"Metadata mismatch: license CKAN='{ckan_record.get('license_id')}' | DataCite='{dc_rights[0].get('rightsIdentifier')}'"
            )

    # Version
    dc_version = (attrs.get("version") or "").lstrip("v").strip()
    ckan_version = (ckan_citation.get("version") or ckan_record.get("version") or "").lstrip("v").strip()
    if dc_version and ckan_version and dc_version != ckan_version:
        issues.append(
            f"Metadata mismatch: version CKAN='{ckan_version}' | DataCite='{dc_version}'"
        )

    # Authors / Creators — compare DataCite creators against citation authors only
    dc_creators = attrs.get("creators", [])
    dc_creator_names = []
    for c in dc_creators:
        if c.get("givenName") or c.get("familyName"):
            name = f"{c.get('givenName', '')} {c.get('familyName', '')}".strip()
        else:
            name = c.get("name", "")
        if name:
            dc_creator_names.append(name)

    ckan_author_names = [
        f"{a.get('given', '')} {a.get('family', '')}".strip()
        for a in ckan_citation.get("author", [])
        if a.get("given") or a.get("family")
    ]

    for dc_name in dc_creator_names:
        if not any(_fuzzy_match(dc_name, n) for n in ckan_author_names):
            issues.append(f"Metadata mismatch: creator '{dc_name}' in DataCite not found in CKAN record")

    for ckan_name in ckan_author_names:
        if not any(_fuzzy_match(ckan_name, dc_name) for dc_name in dc_creator_names):
            issues.append(f"Metadata mismatch: author '{ckan_name}' in CKAN record not found in DataCite")

    # Related works
    dc_related = attrs.get("relatedIdentifiers", [])
    dc_related_ids = {
        _normalize_identifier(r.get("relatedIdentifier", ""), r.get("relatedIdentifierType", ""))
        for r in dc_related
        if r.get("relationType") not in _SKIP_RELATION_TYPES
    }

    ckan_related = ckan_record.get("aggregation-info", [])
    ckan_related_ids = {
        _normalize_identifier(r.get("aggregate-dataset-identifier_code", ""))
        for r in ckan_related
        if r.get("aggregate-dataset-identifier_code")
    }

    for ckan_id in ckan_related_ids:
        if ckan_id and ckan_id not in dc_related_ids:
            issues.append(
                f"Metadata mismatch: related work '{ckan_id}' in CKAN not found in DataCite"
            )

    for rel in dc_related:
        rel_type = rel.get("relationType", "")
        rel_id = _normalize_identifier(
            rel.get("relatedIdentifier", ""), rel.get("relatedIdentifierType", "")
        )
        if rel_type not in _SKIP_RELATION_TYPES and rel_id and rel_id not in ckan_related_ids:
            issues.append(
                f"Metadata mismatch: related identifier '{rel.get('relatedIdentifier')}' ({rel_type}) in DataCite not found in CKAN"
            )

    return issues
