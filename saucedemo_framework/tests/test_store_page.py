import pytest


@pytest.mark.smoke
def test_logout(open_store_page):
    """
        Precondition: User logged in.
        Opens Burger menu and clicks on logout button
        Checks if Login Button is present on Login Page.
    """
    store_page = open_store_page
    login_page = store_page.quick_logout()
    assert login_page.is_login_button_displayed() is True, 'Logout was unsuccessful'


@pytest.mark.regression
def test_burger_menu(open_store_page):
    """
        Precondition: User logged in.
        Opens Burger menu.
        Checks if Burger menu and all buttons inside are displayed.
    """
    store_page = open_store_page
    store_page.open_burger_menu()
    assert store_page.is_burger_menu_filled() is True, 'Burger menu was not opened'


@pytest.mark.regression
def test_open_cart(open_store_page):
    """
        Precondition: User logged in.
        Clicks on Cart button.
        Checks if Cart Page secondary header is displayed.
    """
    store_page = open_store_page
    cart_page = store_page.open_cart()
    assert cart_page.is_cart_header_displayed() is True, 'User is not in cart page/Header was not displayed'


@pytest.mark.smoke
def test_add_to_cart(open_store_page):
    """
        Precondition: User logged in.
        Adds item 'Sauce Labs Backpack' to cart. Opens cart.
        Checks if there's any item in cart and Remove button for 'Sauce Labs Backpack' present.
    """
    store_page = open_store_page
    cart_page = store_page.add_backpack_one_to_cart().open_cart()
    assert cart_page.is_item_and_remove_present() is True, 'Item was not added to cart'
