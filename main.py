from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from info import paths as p


def test_driver():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(chrome_driver, 5)
    chrome_driver.maximize_window()
    chrome_driver.get(p.site_url)

    login_element = wait.until(EC.presence_of_element_located((By.XPATH, p.login_locator)))
    login_element.clear()
    login_element.send_keys(p.login)

    password_element = wait.until(EC.presence_of_element_located((By.XPATH, p.password_locator)))
    password_element.clear()
    password_element.send_keys(p.password)

    login_button_element = wait.until(EC.element_to_be_clickable((By.XPATH, p.login_button_locator)))
    login_button_element.click()

    product_label_element = chrome_driver.find_element(By.XPATH, p.product_label_locator)
    is_product_label = product_label_element.is_displayed()
    assert is_product_label is True, 'Not logged in'
    chrome_driver.quit()

