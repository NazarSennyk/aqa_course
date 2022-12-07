import json
import requests
from qa_automation_hw.utilities.web_ui.decorator_mark_steps import auto_step



@auto_step
class BaseAPI:
    def __init__(self, env):
        self.__base_url = env.base_url_api
        self.__requests = requests
        self.__headers = None

    def get(self, url, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.get(f'{self.__base_url}{url}', headers=headers)
        return response

    def post(self, url, body=None, headers=None):
        if headers is None:
            headers = self.__headers
        json_obj = json.dumps(body)
        response = self.__requests.post(f'{self.__base_url}{url}', headers=headers, json=json_obj)
        return response
