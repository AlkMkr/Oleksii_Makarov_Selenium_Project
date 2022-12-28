from saucedemo_framework.info import paths as p
from saucedemo_framework.utilities.web_ui.base_page import BasePage


class StorePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_burger_menu(self):
        self._click(p.burger_menu_button_locator)
        return self

    def is_burger_menu_located(self):
        return self._is_displayed(p.burger_menu_locator)

    def is_burger_close_button_located(self):
        return self._is_displayed(p.burger_menu_close_locator)

    def close_burger_menu(self):
        self._click(p.burger_menu_close_locator)
        return self

    def is_logout_button_displayed(self):
        return self._is_displayed(p.logout_button_locator)

    def _logout(self):
        self._click(p.logout_button_locator)
        from saucedemo_framework.page_objects.login_page import LoginPage
        return LoginPage(self._driver)

    def add_backpack_one_to_cart(self):
        self._click(p.add_to_cart_backpack_locator_one)
        return self

    def open_cart(self):
        self._click(p.cart_store_button_locator)
        from saucedemo_framework.page_objects.cart_page import CartPage
        return CartPage(self._driver)

    def is_secondary_header_located(self):
        return self._is_displayed(p.header_secondary_container_products)

    def fast_logout(self):
        self.open_burger_menu()._logout()
        from saucedemo_framework.page_objects.login_page import LoginPage
        return LoginPage(self._driver)
