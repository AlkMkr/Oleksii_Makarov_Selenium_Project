import pytest


@pytest.mark.regression
def test_continue_shopping(open_cart_page):
    """
        Precondition: User logged in and Cart page opened.
        Clicks on Continue Shopping Button.
        Checks if Store Page secondary locator is displayed.
    """
    cart_page = open_cart_page
    store_page = cart_page.continue_shopping()
    assert store_page.is_secondary_header_located() is True, 'Wasn`t able to continue shopping'


@pytest.mark.regression
def test_remove_item_from_cart(open_cart_page_with_item):
    """
        Precondition: User logged in, added item in cart and Cart Page opened.
        Opens Cart Page and clicks on remove item button for 'Sauce Labs Backpack' item.
        Checks if there's locator for item in Cart page.
    """
    cart_page = open_cart_page_with_item
    cart_page.click_remove_button()
    assert cart_page.is_there_items_in_cart() is False, 'Item was not removed from the cart'


@pytest.mark.regression
def test_burger_menu_cart(open_cart_page):
    """
        Precondition: User logged in and Cart page opened.
        Clicks on Burger menu button.
        Checks if Burger menu and it's buttons are displayed.
    """
    cart_page = open_cart_page
    burger_menu = cart_page.open_burger_menu()
    assert burger_menu.is_burger_menu_filled() is True, 'Burger menu was not opened'


@pytest.mark.regression
def test_logout_from_cart(open_cart_page):
    """
        Precondition: User logged in and Cart page opened.
        Clicks on Burger Menu and then on Logout button.
        Checks if Login Button is displayed on login Page. Asserting if Logout was successful.
    """
    cart_page = open_cart_page.open_burger_menu()
    login_page = cart_page.logout()
    assert login_page.is_login_button_displayed() is True, 'Logout unsuccessful'


@pytest.mark.smoke
def test_checkout_cart(open_cart_page_with_item):
    """
        Precondition: User logged in, added item in cart and Cart Page opened.
        Clicks on Checkout button on Cart Page.
        Checks if Checkout Page secondary header is displayed.
    """
    cart_page = open_cart_page_with_item
    checkout_page = cart_page.click_checkout()
    assert checkout_page.check_if_checkout_page_header_visible() is True, 'Checkout unsuccessful'
