from saucedemo_framework.info import paths as p
from saucedemo_framework.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def _set_login(self, login_value):
        self._send_keys(p.login_locator, login_value)
        return self

    def _set_password(self, password_value):
        self._send_keys(p.password_locator, password_value)
        return self

    def _press_login(self):
        self._click(p.login_button_locator)
        return self

    def login(self, login_value, password_value):
        self._set_login(login_value)._set_password(password_value)._press_login()
        from saucedemo_framework.page_objects.store_page import StorePage
        return StorePage(self._driver)

    def is_error_message_box_displayed(self):
        return self._is_displayed(p.login_error_message_locator)

    def is_login_button_displayed(self):
        return self._is_displayed(p.login_button_locator)
