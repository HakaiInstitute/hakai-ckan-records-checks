import json
import re

import pandas as pd
import requests
from loguru import logger

DATACITE_API_URL = "https://api.datacite.org/dois"

default = {"data": {"attributes": {"citationCount": -1, "citationsOverTime": []}}}


class Datacite:
    def __init__(self):
        self.url = DATACITE_API_URL

    @logger.catch(default=default)
    def get_doi(self, doi: str) -> dict:
        """Get metadata for a DOI from DataCite"""
        response = requests.get(f"{self.url}/{doi}")
        response.raise_for_status()
        return response.json()
