import requests
import json
import curlify
from requests.structures import CaseInsensitiveDict

class Book(object):

    BASE_PATH = "/BookStore"
    VERSION = "/v1"

    def __init__(self, base_url):
        self.base_url = base_url

    def get_books(self, *args, **kwargs):
        '''
        :param args: for future use
        :param kwargs: for future use
        :return: returns the response
        '''
        version = self.VERSION
        resource = "/Books"
        method = "GET"

        end_point = f"{self.base_url}{self.BASE_PATH}{version}{resource}"
        response = requests.request(method, end_point, *args, **kwargs)
        assert  response.status_code == 200

        return response


    def get_book_by_isbn(self, isbn, *args, **kwargs):
        version = self.VERSION
        resource = "/Books?ISBN="
        method = "GET"

        end_point = f"{self.base_url}{self.BASE_PATH}{version}{resource}{isbn}"
        response = requests.request(method, end_point, *args, **kwargs).json()
        return response



    def create_book(self, payload, token):
        '''

        :param body: Json payload recieved
        :param token: Token sent from test file
        :return:
        '''
        version = self.VERSION
        resource = "/Books"
        method = "POST"
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {}'.format(token)}
        end_point = f"{self.base_url}{self.BASE_PATH}{version}{resource}"
        response = requests.post(end_point, data=json.dumps(payload), headers=headers)
        assert response.status_code == 201
        return response


    def update_book(self, payload, token, isbn):

        version = self.VERSION
        resource = "/Books/"
        method = "PUT"
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {}'.format(token)}
        end_point = f"{self.base_url}{self.BASE_PATH}{version}{resource}{isbn}"
        response = requests.request(method, end_point, data=json.dumps(payload), headers=headers)
        return response

        # headers = CaseInsensitiveDict()
        # headers["accept"] = "application/json"
        # headers["authorization"] = "Basic {}".format(token)
        # headers["Content-Type"] = "application/json"
        #
        # print(payload)
        # resp = requests.put(end_point, headers=headers, data=payload)
        # print(curlify.to_curl(resp.request))
        # print(resp.status_code)




    def delete_books(self, userid, token):
        version = self.VERSION
        resource = "/Books?UserId="
        method = "DELETE"
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {}'.format(token)}

        end_point = f"{self.base_url}{self.BASE_PATH}{version}{resource}{userid}"
        response = requests.request(method, end_point, headers=headers)
        return response

    def delete_book_by_isbn(self, payload, token):
        version = self.VERSION
        resource = "/Book"
        method = "DELETE"
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {}'.format(token)}

        end_point = f"{self.base_url}{self.BASE_PATH}{version}{resource}"
        response = requests.request(method, end_point, data=json.dumps(payload), headers=headers )
        return response