from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:
    @staticmethod
    def create_driver(driver_id: int, is_headless=True):
        if int(driver_id) == 1:
            chrome_option = Options()
            if is_headless:
                chrome_option.add_argument('--headless')
            driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
        elif int(driver_id) == 2:
            driver = Firefox(service=Service(GeckoDriverManager().install()))
        elif int(driver_id) == 3:
            driver = Edge(service=Service(EdgeChromiumDriverManager.install()))
        else:
            driver = Chrome(service=Service(ChromeDriverManager().install()))
        return driver
