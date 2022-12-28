import pytest


@pytest.mark.regression
def test_continue_shopping(open_cart_page):
    cart_page = open_cart_page
    store_page = cart_page.continue_shopping()
    assert store_page.is_secondary_header_located() is True, 'Wasn`t able to continue shopping'


@pytest.mark.regression
def test_remove_item_from_cart(open_cart_page_with_item):
    cart_page = open_cart_page_with_item
    cart_page.press_remove_button()
    assert cart_page.is_remove_button_displayed() is False, 'Item was not removed from the cart'


@pytest.mark.regression
def test_burger_menu_cart(open_cart_page):
    cart_page = open_cart_page
    cart_page.open_burger_menu()
    assert cart_page.is_burger_menu_located() is True, 'Burger menu was not opened'


@pytest.mark.regression
def test_logout_from_cart(open_cart_page):
    cart_page = open_cart_page
    login_page = cart_page.quick_logout()
    assert login_page.is_login_button_displayed() is True, 'Logout unsuccessful'


@pytest.mark.smoke
def test_checkout_cart(open_cart_page_with_item):
    cart_page = open_cart_page_with_item
    checkout_page = cart_page.click_checkout()
    assert checkout_page.check_if_checkout_page_header_visible() is True, 'Checkout unsuccessful'

