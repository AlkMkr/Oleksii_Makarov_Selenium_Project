from saucedemo_framework.utilities.web_ui.base_page import BasePage
from saucedemo_framework.locators import locators as p
from saucedemo_framework.page_objects.cart_page import CartPage
from saucedemo_framework.page_objects.overview_page import OverviewPage
from saucedemo_framework.page_objects.login_page import LoginPage


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_if_checkout_page_header_visible(self) -> bool:
        """
            Checks if secondary header for Checkout Page is displayed.
            Returns True of False.
        """
        return self._is_displayed(p.header_secondary_container_checkout)

    def checkout_cancel(self) -> CartPage:
        """
            Clicks on Cancel button on checkout page.
            Returns a copy of CartPage class, allowing to use its methods.
        """
        self._click(p.checkout_cancel_button)
        return CartPage(self._driver)

    def _set_first_name(self, first_name_value) -> CheckoutPage:
        """
            Takes parameter and sends it to First Name Field on Checkout Page.
        """
        self._send_keys(p.checkout_first_name_field, first_name_value, is_clear=False)
        return self

    def _set_last_name(self, second_name_value) -> CheckoutPage:
        """
            Takes parameter and sends it to Last Name Field on Checkout Page.
        """
        self._send_keys(p.checkout_last_name_field, second_name_value, is_clear=False)
        return self

    def _set_postal_code(self, postal_code_value) -> CheckoutPage:
        """
            Takes parameter and sends it to Postal Code Field on Checkout Page.
        """
        self._send_keys(p.checkout_postal_code_field, postal_code_value, is_clear=False)
        return self

    def _continue_checkout_button(self) -> CheckoutPage:
        """
            Clicks on Continue button on Checkout Page.
        """
        self._click(p.checkout_continue_button)
        return self

    def full_continue_checkout(self, first_name_value, second_name_value, postal_code_value) -> OverviewPage:
        """
            Takes three parameters and send them to First Name field, Last Name field and Postal Code field respectively.
            Clicks on Continue Checkout button.
            Returns a copy of OverviewPage class, allowing to use its methods.
        """
        self._set_first_name(first_name_value)._set_last_name(second_name_value)._set_postal_code(
            postal_code_value)._continue_checkout_button()
        return OverviewPage(self._driver)

    def _is_checkout_error_message_visible(self) -> bool:
        """
            Checks if error message is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.checkout_error_container)

    def _is_first_name_error_visible(self) -> bool:
        """
            Checks if First Name Error is visible.
            Returns True or False.
        """
        return self._is_displayed(p.checkout_error_first_name)

    def _is_last_name_error_visible(self) -> bool:
        """
            Checks if Last Name Error is visible.
            Returns True or False.
        """
        return self._is_displayed(p.checkout_error_last_name)

    def _is_postal_code_error_visible(self) -> bool:
        """
            Checks if Postal Code Error is visible.
            Returns True or False.
        """
        return self._is_displayed(p.checkout_error_postal_code)

    def is_any_error_message_visible(self) -> bool:
        """
            Checks if Error Message is visible and if it's one of the three: First Name, Last Name, Postal Code.
            Returns True or False.
        """
        return self._is_checkout_error_message_visible() and any([self._is_first_name_error_visible(),
                                                                  self._is_last_name_error_visible(),
                                                                  self._is_postal_code_error_visible()])

    def _open_burger_menu(self) -> CheckoutPage:
        """
            Opens Burger Menu
        """
        self._click(p.burger_menu_button_locator)
        return self

    def close_burger_menu(self) -> CheckoutPage:
        """
            Closes Burger Menu
        """
        self._click(p.burger_menu_close_locator)
        return self

    def _logout(self) -> CheckoutPage:
        """
            Clicks on Logout button in already opened burger menu.
            Returns a copy of LoginPage class, allowing to use its methods.
        """
        self._click(p.logout_button_locator)
        return self

    def quick_logout(self):
        """
            Opens burger menu and clicks on logout button.
            Returns a copy of LoginPage class, allowing to use its methods
        """
        self._open_burger_menu()._logout()
        return LoginPage(self._driver)
