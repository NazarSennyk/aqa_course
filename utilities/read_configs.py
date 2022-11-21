import configparser


abs_path = r'C:\Users\nazarii.sennyk\PycharmProjects\QA_automation_course\qa_automation_hw\configurations\configurations.ini'
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
