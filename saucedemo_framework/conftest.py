import pytest
from saucedemo_framework.page_objects.login_page import LoginPage
from saucedemo_framework.utilities.config_parser import ReadConfig
from saucedemo_framework.utilities.driver_factory import DriverFactory


@pytest.fixture()
def create_driver():
    """
        Creates webdriver based on data in config. Opens site based on config data. Maximizes window. Yields driver.
        Can be headless.
    """
    driver = DriverFactory.create_driver(driver_id=ReadConfig.get_driver_id(),
                                         is_headless=ReadConfig.get_headless())
    driver.maximize_window()
    driver.get(ReadConfig.get_base_url())
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    """
        Repeats sequence of create_driver fixture. Returns Page object of Login Page.
    """
    return LoginPage(create_driver)


@pytest.fixture()
def open_store_page(open_login_page):
    """
        Repeats sequence of open_login_page fixture. Logins into the site using data from config.
        Returns page object of Store Page.
    """
    store_page = open_login_page.login(ReadConfig.get_login(), ReadConfig.get_password())
    return store_page


@pytest.fixture()
def open_cart_page(open_store_page):
    """
        Repeats sequence of open_store_page fixture. Opens cart from Store page.
        Returns page object of Cart Page.
    """
    cart_page = open_store_page.open_cart()
    return cart_page


@pytest.fixture()
def open_cart_page_with_item(open_store_page):
    """
        Repeats sequence of open_store_page fixture. Adds "Sauce Labs Backpack" item to the cart. Opens cart.
        Returns page object of Cart Page.
    """
    cart_page = open_store_page.add_backpack_one_to_cart().open_cart()
    return cart_page


@pytest.fixture()
def open_checkout_page(open_cart_page_with_item):
    """
        Repeats sequence of open_cart_page_with_item fixture. Clicks Checkout button.
        Returns page object of Checkout Page.
    """
    checkout_page = open_cart_page_with_item.click_checkout()
    return checkout_page


@pytest.fixture()
def open_overview_page(open_checkout_page):
    """
        Repeats sequence of open_checkout_page fixture. Fill fields of checkout page with data from config.
        Continues Checkout.
        Returns page object of Overview Page.
    """
    overview_page = open_checkout_page.full_continue_checkout(ReadConfig.get_first_name(), ReadConfig.get_last_name(),
                                                              ReadConfig.get_postal_code())
    return overview_page


@pytest.fixture()
def open_complete_page(open_overview_page):
    """
        Repeats sequence of open_overview_page fixture. Clicks on complete overview button.
        Returns page object of Complete Page.
    """
    complete_page = open_overview_page.finish_overview()
    return complete_page
