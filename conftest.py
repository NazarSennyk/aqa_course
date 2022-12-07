import json
from contextlib import suppress
import pytest
from qa_automation_hw.data_classes.person import Person
from qa_automation_hw.page_objects.login_page import LoginPage
from qa_automation_hw.utilities.configuration import Configuration
from qa_automation_hw.utilities.driver_factory import DriverFactory
from qa_automation_hw.utilities.read_configs import Read_config
import allure


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'rep_' + rep.when, rep)
    return rep


@pytest.fixture()
def create_driver(request):
    driver_chrome = DriverFactory.create_driver(driver_id=Read_config.get_browser_id())
    driver_chrome.maximize_window()
    driver_chrome.get(Read_config.get_base_urt())
    yield driver_chrome
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver_chrome.get_screenshot_as_png(), name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver_chrome.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def log_in_user(open_login_page, env):
    open_login_page.open_login_window()
    return open_login_page.login(env.cell_phone, env.password)


@pytest.fixture(scope='session')
def env():
    with open(r'C:\Users\Admin\PycharmProjects\pythonProject\qa_automation_hw\configuration\configuration.json') as f:
        data = f.read()
        json_to_dict = json.loads(data)
    config = Configuration(**json_to_dict)
    return config


@pytest.fixture()
def crate_person():
    return Person()





