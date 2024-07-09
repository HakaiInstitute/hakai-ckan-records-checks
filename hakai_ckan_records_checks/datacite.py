import json

import requests
from loguru import logger

DATACITE_API_URL = "https://api.datacite.org/dois"

RELATIONSHIPS_TRACKED = [
    "references",
    "citations",
    "parts",
    "partOf",
    "versions",
    "versionOf",
]

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
            error = json.loads(response.text)['errors'][0]
            msg = f"Failed to retrieve DOI from dataCite [{error['status']}] {error['title']}: {doi}"
            logger.error(msg)
            return {}, msg
        return response.json(), None


def get_datacite_summary(record):
    if not record:
        return {}
    if record['data']['attributes']['citationCount']>0:
        logger.info(f"Found citation count: {record['data']['attributes']['citationCount']}")
    return {
        "citation_count": record["data"]["attributes"][
            "citationCount"
        ],
        "citations_over_time": record["data"]["attributes"][
            "citationsOverTime"
        ],
        "relationships": {relationship: attrs['data'] for relationship, attrs in record['data']['relationships'].items() if relationship in RELATIONSHIPS_TRACKED and attrs['data']}
    }
