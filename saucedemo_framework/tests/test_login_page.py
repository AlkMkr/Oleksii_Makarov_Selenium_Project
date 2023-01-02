import pytest

from saucedemo_framework.utilities.config_parser import ReadConfig


@pytest.mark.smoke
def test_login_page(open_login_page):
    """
        Precondition: none.
        Fills Login and Password field with info from config. Clicks on Login Button
        Checks if Store page secondary Header is displayed.
    """
    login_page = open_login_page
    store_page = login_page.login(ReadConfig.get_login(), ReadConfig.get_password())
    assert store_page.is_secondary_header_located() is True, 'User was not logged in'


@pytest.mark.regression
@pytest.mark.parametrize('login_value, password_value',
                         [('', ''), (ReadConfig.get_login(), ''),
                          ('wrong answer', 'wrong again'), ('', ReadConfig.get_password()),
                          (ReadConfig.get_login(), 'try again'),
                          ('it won`t work', ReadConfig.get_password())],
                         ids=['empty spaces', 'empty password', 'wrong data', 'empty login', 'wrong password',
                              'wrong login'])
def test_negative_login_page(open_login_page, login_value, password_value):
    """
        Precondition: none.
        Fills Login and Password Field with either wrong data, empty field, or incomplete data.
        Checks if error messages are displayed and one of the three variations:
        Login Missing, Password Missing, Login or Password don't match.
    """
    login_page = open_login_page
    login_page.login(login_value, password_value)
    assert login_page.is_any_error_displayed() is True, 'You`ve logged in despite having' \
                                                        ' wrong login or password'
