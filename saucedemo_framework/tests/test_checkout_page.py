import pytest
from saucedemo_framework.utilities.config_parser import ReadConfig as RC


@pytest.mark.smoke
def test_proper_checkout(open_checkout_page, env):
    """
        Precondition: User Logged In, added item in cart, and clicked Checkout button.
        Fills First Name, Last Name and Postal Code fields with info from config. Clicks Continue Button.
        Checks if Overview Page Secondary Header is displayed.
    """
    checkout_page = open_checkout_page
    overview_page = checkout_page.full_continue_checkout(env.first_name, env.last_name,
                                                         env.postal_code)
    assert overview_page.is_overview_header_title_visible() is True, 'Checkout was not successful'


@pytest.mark.regression
@pytest.mark.parametrize('first_name, last_name, postal_code', [
    ('', 'env.last_name', 'env.postal_code'),
    ('env.first_name', '', 'env.postal_code'),
    ('env.first_name', 'env.last_name', ''), ('', '', '')],
                         ids=['empty_name', 'empty_last_name', 'empty_postal_code', 'empty_data'])
def test_negative_checkout(open_checkout_page, first_name, last_name, postal_code, env):
    """
        Precondition: User Logged In, added item in cart, and clicked Checkout button.
        Fills First Name, Last Name and Postal Code fields with info from config, but leaves at least one field empty.
        Checks if Error message was displayed and with proper error message
    """
    unstringed = ['', '', '']
    data = [first_name, last_name, postal_code]
    for index, param in enumerate(data):
        if param:
            unstringed[index] = eval(param)
    checkout_page = open_checkout_page
    checkout_page.full_continue_checkout(unstringed[0], unstringed[1], unstringed[2])
    assert checkout_page.is_any_error_message_visible() is True, 'You made checkout with wrong data'


@pytest.mark.regression
def test_checkout_logout(open_checkout_page):
    """
        Precondition: User Logged In, added item in cart, and clicked Checkout button.
        Clicks on Burger Menu and then on Logout button.
        Checks if Login Button is displayed on login Page. Asserting if Logout was successful.
    """
    checkout_page = open_checkout_page
    login_page = checkout_page.quick_logout()
    assert login_page.is_login_button_displayed() is True, 'Logout unsuccessful'
