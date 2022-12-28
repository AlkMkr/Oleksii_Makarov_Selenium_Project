from saucedemo_framework.utilities.web_ui.base_page import BasePage
from saucedemo_framework.info import paths as p


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_remove_button_displayed(self):
        return self._is_displayed(p.remove_saucelab_backpack_cart_locator)

    def press_remove_button(self):
        self._click(p.remove_saucelab_backpack_cart_locator)
        return self

    def is_cart_header_displayed(self):
        return self._is_displayed(p.header_secondary_container_cart)

    def continue_shopping(self):
        self._click(p.cart_button_continue_shopping)
        from saucedemo_framework.page_objects.store_page import StorePage
        return StorePage(self._driver)

    def click_checkout(self):
        self._click(p.cart_checkout_button)
        from saucedemo_framework.page_objects.checkout_page import CheckoutPage
        return CheckoutPage(self._driver)

    def open_burger_menu(self):
        self._click(p.burger_menu_button_locator)
        return self

    def is_burger_menu_located(self):
        return self._is_displayed(p.burger_menu_locator)

    def close_burger_menu(self):
        self._click(p.burger_menu_close_locator)
        return self

    def _logout(self):
        self._click(p.logout_button_locator)
        from saucedemo_framework.page_objects.login_page import LoginPage
        return LoginPage(self._driver)

    def quick_logout(self):
        self.open_burger_menu()._logout()
        from saucedemo_framework.page_objects.login_page import LoginPage
        return LoginPage(self._driver)
