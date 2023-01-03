from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.chrome.options import Options as C_Options
from selenium.webdriver.firefox.options import Options as F_Options
from selenium.webdriver.edge.options import Options as E_Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:
    @staticmethod
    def create_driver(driver_id: int, is_headless=True):
        """
            Takes parameter (from 1 to 3). And creates a driver based on number:
            1 - Chrome; 2 - Firefox; 3 - Edge; none or any other number - Chrome.
            Return created driver.
        """
        if int(driver_id) == 1:
            chrome_option = C_Options()
            if is_headless:
                chrome_option.add_argument('--headless')
            driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
        elif int(driver_id) == 2:
            firefox_option = F_Options()
            if is_headless:
                firefox_option.add_argument('--headless')
            driver = Firefox(service=Service(GeckoDriverManager().install()), options=firefox_option)
        elif int(driver_id) == 3:
            edge_option = E_Options()
            if is_headless:
                edge_option.add_argument('--headless')
            driver = Edge(service=Service(EdgeChromiumDriverManager.install()), options=edge_option)
        else:
            chrome_option = C_Options()
            if is_headless:
                chrome_option.add_argument('--headless')
            driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
        return driver
