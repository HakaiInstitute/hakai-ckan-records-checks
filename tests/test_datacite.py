import pytest

from hakai_ckan_records_checks.datacite import Datacite

DOIs = ["10.21966/1.715784"]


@pytest.mark.parametrize("doi", DOIs)
def test_get_doi(doi):
    datacite = Datacite()
    response = datacite.get_doi(doi)
    assert doi
    assert response["data"]["id"] == doi
