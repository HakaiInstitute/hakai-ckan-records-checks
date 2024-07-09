import json
import re

import pandas as pd
import requests
from loguru import logger

DATACITE_API_URL = "https://api.datacite.org/dois"


class Datacite:
    def __init__(self):
        self.url = DATACITE_API_URL

    @logger.catch(default={})
    def get_doi(self, doi: str):
        """Get metadata for a DOI from DataCite"""
        response = requests.get(f"{self.url}/{doi}")
        if response.status_code != 200:
            error = json.loads(response.text)['errors'][0]
            msg = f"Failed to retrieve DOI from dataCite [{error['status']}] {error['title']}: {doi}"
            logger.error(msg)
            return {}, msg
        return response.json(), None

