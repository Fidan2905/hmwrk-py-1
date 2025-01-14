import requests


class Yougile:
    def __init__(self, url):
        self.url = url

    def get_token(self, login, password, companyId):
        creds = {"login": login, "password": password, "company_id": companyId}
        resp = requests.post(self.url + "/auth/keys", json=creds)
        return resp.json()["key"]

    def get_list_projects(self, token):
        headers = {"Authorization": "Bearer " + token}
        resp = requests.get(self.url + "/projects", headers=headers)
        return resp.json()

    def get_project_by_id(self, token, id):
        headers = {"Authorization": "Bearer " + token}
        resp = requests.get(self.url + "/projects/" + id, headers=headers)
        return resp.json()

    def create_project(self, token, companyname):
        headers = {"Authorization": "Bearer " + token}
        body = {"title": companyname}
        pr = "/projects"
        resp = requests.post(self.url + pr, headers=headers, json=body)
        return resp.json()

    def put_project_by_id_title(self, token, id, title):
        h = {"Authorization": "Bearer " + token}
        body = {"title": title}
        p = "/projects/"
        resp = requests.get(self.url + p + id, headers=h, json=body)
        return resp.json()