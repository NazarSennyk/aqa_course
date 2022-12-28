import configparser
from qa_automation_course.CONSTANTS import ROOT_DIR

abs_path = f'{ROOT_DIR}/configuration/configurations.ini'
config = configparser.RawConfigParser()
config.read(abs_path)


class Read_config:
    @staticmethod
    def get_base_urt():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_user_name():
        return config.get('user_data', 'login')

    @staticmethod
    def get_browser_id():
        return config.get('browser_data', 'browser_id')
