import requests


class ProjectYouGile:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def create_project(self, title):
        payload = {
            "title": title
        }
        response = requests.post(f"{self.base_url}/api-v2/projects",
                                 headers=self.headers, json=payload)
        return response

    def get_project(self, project_id):
        response = requests.get(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers)
        return response

    def update_project(self, project_id, title):
        payload = {
            "title": title
        }
        response = requests.put(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers, json=payload)
        return response
