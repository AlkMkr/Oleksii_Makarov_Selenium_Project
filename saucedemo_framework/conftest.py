import pytest

from saucedemo_framework.page_objects.checkout_page import CheckoutPage
from saucedemo_framework.page_objects.login_page import LoginPage
from saucedemo_framework.page_objects.store_page import StorePage
from saucedemo_framework.utilities.config_parser import ReadConfig
from saucedemo_framework.utilities.driver_factory import DriverFactory


@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(driver_id=ReadConfig.get_driver_id(),
                                         is_headless=ReadConfig.get_headless())
    driver.maximize_window()
    driver.get(ReadConfig.get_base_url())
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def open_store_page(open_login_page):
    store_page = open_login_page.login(ReadConfig.get_login(), ReadConfig.get_password())
    return store_page


@pytest.fixture()
def no_login_store_page(create_driver):
    return StorePage(create_driver)


@pytest.fixture()
def open_cart_page(open_store_page):
    cart_page = open_store_page.open_cart()
    return cart_page


@pytest.fixture()
def open_cart_page_with_item(open_store_page):
    cart_page = open_store_page.add_backpack_one_to_cart().open_cart()
    return cart_page


@pytest.fixture()
def open_checkout_page(open_cart_page_with_item):
    checkout_page = open_cart_page_with_item.click_checkout()
    return checkout_page


@pytest.fixture()
def open_overview_page(open_checkout_page):
    overview_page = open_checkout_page.full_continue_checkout(ReadConfig.get_first_name(), ReadConfig.get_last_name(),
                                                              ReadConfig.get_postal_code())
    return overview_page


@pytest.fixture()
def open_complete_page(open_overview_page):
    complete_page = open_overview_page.finish_overview()
    return complete_page
