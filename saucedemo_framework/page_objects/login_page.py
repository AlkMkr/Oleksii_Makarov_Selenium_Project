from saucedemo_framework.locators import locators as p
from saucedemo_framework.utilities.decorator import auto_add_step
from saucedemo_framework.utilities.web_ui.base_page import BasePage


@auto_add_step
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def _set_login(self, login_value: str):
        """
            Takes parameter and sends it to Login Field.
        """
        self._send_keys(p.login_locator, login_value)
        return self

    def _set_password(self, password_value: str):
        """
            Takes parameter and sends it to Password Field.
        """
        self._send_keys(p.password_locator, password_value)
        return self

    def _press_login(self):
        """
            Clicks on Login Button.
        """
        self._click(p.login_button_locator)
        return self

    def login(self, login_value: str, password_value: str):
        """
            Takes two parameters and sends them to Login field and Password field respectively.
            Returns a page object StorePage, allowing to use its methods.
        """
        self._set_login(login_value)._set_password(password_value)._press_login()
        from saucedemo_framework.page_objects.store_page import StorePage
        return StorePage(self._driver)

    def _is_error_message_box_visible(self) -> bool:
        """
            Checks if Error message box is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.login_error_message_locator)

    def _is_login_missing_error_visible(self) -> bool:
        """
            Checks if error message displayed is "Epic sadface: Username is required".
            Return True or False.
        """
        return self._is_displayed(p.login_error_missing_login)

    def _is_password_missing_error_visible(self) -> bool:
        """
            Checks if error message displayed is "Epic sadface: Password is required".
            Return True or False.
        """
        return self._is_displayed(p.login_error_missing_password)

    def _is_login_or_password_wrong_error_visible(self) -> bool:
        """
            Checks if error message displayed is "Epic sadface: Username and password do not match any user in this service".
            Return True or False.
        """
        return self._is_displayed(p.login_error_wrong_login_password)

    def is_any_error_displayed(self) -> bool:
        """
            Checks if error message is located and any of the three variations:
            Missing Login, Missing Password, Login or Password don't match.
            Returns True or False.
        """
        return self._is_error_message_box_visible() and any(
            [self._is_login_missing_error_visible(), self._is_password_missing_error_visible(),
             self._is_login_or_password_wrong_error_visible()])

    def is_login_button_displayed(self) -> bool:
        """
            Checks if Login button is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.login_button_locator)
