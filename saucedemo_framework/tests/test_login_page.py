import pytest

from saucedemo_framework.utilities.config_parser import ReadConfig


@pytest.mark.smoke
def test_login_page(open_login_page):
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
    login_page = open_login_page
    login_page.login(login_value, password_value)
    assert login_page.is_error_message_box_displayed() is True, 'You`ve logged in despite having' \
                                                                ' wrong login or password'
