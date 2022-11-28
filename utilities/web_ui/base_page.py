from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 10)

    __login_button_locator = (By.XPATH, '//a[@href="#enter"]')

    def __wait_until_element_located(self, locator: tuple):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def __wait_until_element_clickable(self, locator: tuple):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def __wait_until_element_visible(self, locator: tuple):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def open_login_window(self):
        login_button_element = self.__wait.until(EC.element_to_be_clickable(self.__login_button_locator))
        login_button_element.click()

    def _send_keys(self, locator: tuple, value: str):
        element = self.__wait_until_element_located(locator)
        element.clear()
        element.send_keys(value)

    def _click(self, locator: tuple):
        self.__wait_until_element_visible(locator)
        element = self.__wait_until_element_clickable(locator)
        element.click()

    def _is_visible(self, locator: tuple):
        try:
            self.__wait_until_element_visible(locator)
            return True
        except TimeoutException:
            return False


