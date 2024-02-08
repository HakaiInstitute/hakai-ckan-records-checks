import requests


class CKAN:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def __equal__(self, other):
        return self.base_url == other.base_url and self.api_key == other.api_key

    def get_all_records(self):
        url = f"{self.base_url}/api/3/action/package_list"
        headers = {"Authorization": self.api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_record(self, record_id):
        url = f"{self.base_url}/api/3/action/package_show?id={record_id}"
        headers = {"Authorization": self.api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
