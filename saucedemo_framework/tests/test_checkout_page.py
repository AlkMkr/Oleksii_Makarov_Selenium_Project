import pytest

from saucedemo_framework.utilities.config_parser import ReadConfig as RC


@pytest.mark.smoke
def test_proper_checkout(open_checkout_page):
    checkout_page = open_checkout_page
    overview_page = checkout_page.full_continue_checkout(RC.get_first_name(), RC.get_last_name(),
                                                         RC.get_postal_code())
    assert overview_page.is_overview_header_title_visible() is True, 'Checkout was not successful'


@pytest.mark.regression
@pytest.mark.parametrize('first_name, last_name, postal_code', [
    ('', RC.get_last_name(), RC.get_postal_code()),
    (RC.get_first_name(), '', RC.get_postal_code()),
    (RC.get_first_name(), RC.get_last_name(), ''), ('', '', '')],
                         ids=['empty_name', 'empty_last_name', 'empty_postal_code', 'empty_data'])
def test_negative_checkout(open_checkout_page, first_name, last_name, postal_code):
    checkout_page = open_checkout_page
    checkout_page.full_continue_checkout(first_name, last_name, postal_code)
    assert checkout_page.is_checkout_error_message_visible() is True, 'You made checkout with wrong data'


@pytest.mark.regression
def test_checkout_logout(open_checkout_page):
    checkout_page = open_checkout_page
    login_page = checkout_page.quick_logout()
    assert login_page.is_login_button_displayed() is True, 'Logout unsuccessful'
