import json
from qa_automation_hw.conftest import env
import requests


class BaseAPI:
    def __init__(self):
        self.__base_url = env()
        self.__requests = requests
        self.__headers = None

    def get(self, url, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.get(f'{self.__base_url}{url}', headers=headers)
        return response

    def post(self, url, body={'tests': '12324'}, headers=None):
        if headers is None:
            headers = self.__headers
        json_obj = json.dumps(body)
        response = self.__requests.post(f'{self.__base_url}{url}', headers=headers, json=json_obj)
        return response
        