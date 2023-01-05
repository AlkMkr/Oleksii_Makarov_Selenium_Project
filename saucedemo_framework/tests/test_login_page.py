import pytest


@pytest.mark.smoke
def test_login_page(open_login_page, env):
    """
        Precondition: none.
        Fills Login and Password field with info from config. Clicks on Login Button
        Checks if Store page secondary Header is displayed.
    """
    login_page = open_login_page
    store_page = login_page.login(env.login, env.password)
    assert store_page.is_secondary_header_located() is True, 'User was not logged in'


@pytest.mark.regression
@pytest.mark.parametrize('login_value, password_value',
                         [('', ''), ('env.login', ''), ('wrong answer', 'wrong again'), ('', 'env.password'),
                          ('env.login', 'try again'), ('it won`t work', 'env.password')],
                         ids=['empty spaces', 'empty password', 'wrong data', 'empty login', 'wrong password',
                              'wrong login'])
def test_negative_login_page(open_login_page, login_value, password_value, env):
    """
        Precondition: none.
        Fills Login and Password Field with either wrong data, empty field, or incomplete data.
        Checks if error messages are displayed and one of the three variations:
        Login Missing, Password Missing, Login or Password don't match.
    """
    unstringed = ['', '']
    data = [login_value, password_value]
    for index, param in enumerate(data):
        if param.startswith('env.'):
            if param:
                unstringed[index] = eval(param)
        else:
            unstringed[index] = param
    login_page = open_login_page
    login_page.login(unstringed[0], unstringed[1])
    assert login_page.is_any_error_displayed() is True, 'You`ve logged in despite having' \
                                                        ' wrong login or password'
