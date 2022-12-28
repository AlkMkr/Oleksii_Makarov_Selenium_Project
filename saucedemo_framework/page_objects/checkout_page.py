from saucedemo_framework.utilities.web_ui.base_page import BasePage
from saucedemo_framework.info import paths as p


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_if_checkout_page_header_visible(self):
        return self._is_displayed(p.header_secondary_container_checkout)

    def checkout_cancel(self):
        self._click(p.checkout_cancel_button)
        from saucedemo_framework.page_objects.cart_page import CartPage
        return CartPage(self._driver)

    def _set_first_name(self, first_name_value):
        self._send_keys(p.checkout_first_name_field, first_name_value, is_clear=False)
        return self

    def _set_last_name(self, second_name_value):
        self._send_keys(p.checkout_last_name_field, second_name_value, is_clear=False)
        return self

    def _set_postal_code(self, postal_code_value):
        self._send_keys(p.checkout_postal_code_field, postal_code_value, is_clear=False)
        return self

    def _continue_checkout_button(self):
        self._click(p.checkout_continue_button)
        return self

    def full_continue_checkout(self, first_name_value, second_name_value, postal_code_value):
        self._set_first_name(first_name_value)._set_last_name(second_name_value)._set_postal_code(
            postal_code_value)._continue_checkout_button()
        from saucedemo_framework.page_objects.overview_page import OverviewPage
        return OverviewPage(self._driver)

    def is_checkout_error_message_visible(self):
        return self._is_displayed(p.checkout_error_container)

    def _open_burger_menu(self):
        self._click(p.burger_menu_button_locator)
        return self

    def close_burger_menu(self):
        self._click(p.burger_menu_close_locator)
        return self

    def _logout(self):
        self._click(p.logout_button_locator)
        from saucedemo_framework.page_objects.login_page import LoginPage
        return LoginPage(self._driver)

    def quick_logout(self):
        self._open_burger_menu()._logout()
        from saucedemo_framework.page_objects.login_page import LoginPage
        return LoginPage(self._driver)
