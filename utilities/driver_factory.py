from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
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
            driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif int(driver_id) == DriverFactory.firefox:
            driver = Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif int(driver_id) == DriverFactory.edge:
            driver = Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
        return driver
