import requests

class Account(object):

    BASE_PATH = "/Account"
    VERSION = "/v1"

    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password


    def create_user(self, *args, **kwargs):
        version = self.VERSION
        resource = "/User"
        method = "POST"

        body = {
            "userName": self.username,
            "password": self.password
        }

        end_point = f"{self.base_url}{self.BASE_PATH}{version}{resource}"
        response = requests.request(method, end_point, *args, json=body, **kwargs)

        return response

    def generate_token(self, *args, **kwargs):
        version = self.VERSION
        resource = "/GenerateToken"
        method = "POST"

        body = {
            "userName": self.username,
            "password": self.password
        }

        end_point = f"{self.base_url}{self.BASE_PATH}{version}{resource}"
        response = requests.request(method, end_point, *args, json=body, **kwargs)
        return response


    def delete_user(self, userid, token):
        version = self.VERSION
        resource = "/User/"
        method = "DELETE"
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {}'.format(token)}

        end_point = f"{self.base_url}{self.BASE_PATH}{version}{resource}{userid}"
        response = requests.request(method, end_point, headers=headers)
        return response





