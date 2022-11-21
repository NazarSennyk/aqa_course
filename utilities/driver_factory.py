from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:
    chrome = 1
    firefox = 2
    edge = 3

    @staticmethod
    def create_driver(driver_id):
        if int(driver_id) == DriverFactory.chrome:
            driver = Chrome(service=Service(ChromeDriverManager().install()))
        elif int(driver_id) == DriverFactory.firefox:
            driver = Firefox(service=Service(GeckoDriverManager().install()))
        elif int(driver_id) == DriverFactory.edge:
            driver = Edge(service=Service(EdgeChromiumDriverManager().install()))
        else:
            driver = Chrome(service=Service(ChromeDriverManager().install()))
        return driver
