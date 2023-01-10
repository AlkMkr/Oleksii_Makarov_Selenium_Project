import pytest


@pytest.mark.smoke
def test_cancel_overview(open_overview_page):
    """
        Precondition: User Loggen in. Added item in cart and Checked out to Overview page.
        Clicks on Cancel Overview button.
        Checks if Store Page secondary header is displayed.
    """
    overview = open_overview_page
    store_page = overview.cancel_overview()
    assert store_page.is_secondary_header_located() is True, 'Cancellation was unsuccessful'


@pytest.mark.regression
def test_logout_from_overview(open_overview_page):
    """
        Precondition: User Loggen in. Added item in cart and Checked out to Overview page.
        Open Burger menu and clicks Logout.
        Checks if Login button is present in Login Page.
    """
    overview = open_overview_page
    login_page = overview.open_burger_menu().logout()
    assert login_page.is_login_button_displayed() is True, 'Logout unsuccessful'


@pytest.mark.smoke
def test_complete_overview(open_overview_page):
    """
        Precondition: User Loggen in. Added item in cart and Checked out to Overview page.
        Clicks on Complete button.
        Checks if Complete Page secondary header is displayed.
    """
    overview = open_overview_page
    complete_page = overview.finish_overview()
    assert complete_page.is_header_visible() is True, 'Complete operation unsuccessful'


@pytest.mark.regression
def test_complete_page(open_complete_page):
    """
        Precondition: User Loggen in. Added item in cart and Checked out to Overview page. Overview completed.
        Clicks Back Home button.
        Checks if Store Page secondary Header is displayed.
    """
    complete_page = open_complete_page
    store_page = complete_page.complete_back_home()
    assert store_page.is_secondary_header_located() is True, 'Back home Button unsuccessful'


@pytest.mark.regression
def test_complete_page_logout(open_complete_page):
    """
        Precondition: User Loggen in. Added item in cart and Checked out to Overview page. Overview completed.
        Open Burger menu and clicks Logout.
        Checks if Login button is present in Login Page.
    """
    complete_page = open_complete_page
    login_page = complete_page.open_burger_menu().logout()
    assert login_page.is_login_button_displayed() is True, 'Logout was unsuccessful'
