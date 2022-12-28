import json
from contextlib import suppress
import pytest
from qa_automation_hw.page_objects.login_page import LoginPage
from qa_automation_hw.CONSTANTS import ROOT_DIR
from qa_automation_hw.utilities.configuration import Configuration
from qa_automation_hw.utilities.driver_factory import DriverFactory
import allure


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'rep_' + rep.when, rep)
    return rep


@pytest.fixture()
def create_driver(env, request):
    driver_chrome = DriverFactory.create_driver(driver_id=env.browser_id)
    driver_chrome.maximize_window()
    yield driver_chrome
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver_chrome.get_screenshot_as_png(), name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver_chrome.quit()


@pytest.fixture()
def open_login_page(create_driver, env):
    create_driver.get(f'{env.base_url}')
    return LoginPage(create_driver)


@pytest.fixture()
def log_in_user(open_login_page, env):
    open_login_page.open_login_window()
    return open_login_page.login(env.cell_phone, env.password)


@pytest.fixture(scope='session')
def env():
    with open(f'{ROOT_DIR}/configuration/configuration.json') as f:
        data = f.read()
        json_to_dict = json.loads(data)
    config = Configuration(**json_to_dict)
    return config








