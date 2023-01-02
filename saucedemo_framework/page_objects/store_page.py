from saucedemo_framework.locators import locators as p
from saucedemo_framework.utilities.web_ui.base_page import BasePage


class StorePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_burger_menu(self):
        """
            Opens burger menu.
        """
        self._click(p.burger_menu_button_locator)
        return self

    def _is_burger_menu_located(self):
        """
            Checks if burger menu is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.burger_menu_locator)

    def _is_burger_menu_about_displayed(self):
        """
            Checks if About button in burger menu is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.burger_about_button_locator)

    def _is_burger_menu_reset_displayed(self):
        """
            Checks if Reset button in burger menu is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.burger_reset_button_locator)

    def _is_burger_menu_all_items_displayed(self):
        """
            Checks if All Items button in burger menu is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.burger_all_items_button_locator)

    def _is_burger_menu_logout_displayed(self):
        """
            Checks if Logout button in burger menu is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.logout_button_locator)

    def _is_burger_menu_close_button_located(self):
        """
            Checks if Close(x) button in burger menu is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.burger_menu_close_locator)

    def is_burger_menu_filled(self):
        """
            Checks if burger menu and all buttons in it are displayed.
            Returns True or False.
        """
        return all([self._is_burger_menu_located(), self._is_burger_menu_about_displayed(),
                    self._is_burger_menu_reset_displayed(), self._is_burger_menu_all_items_displayed,
                    self._is_burger_menu_logout_displayed(), self._is_burger_menu_close_button_located()])

    def close_burger_menu(self):
        """
            Clicks on Close(x) button in burger menu.
        """
        self._click(p.burger_menu_close_locator)
        return self

    def _logout(self):
        """
            Clicks on Logout button in already opened burger menu.
            Returns a copy of LoginPage class, allowing to use its methods.
        """
        self._click(p.logout_button_locator)
        from saucedemo_framework.page_objects.login_page import LoginPage
        return LoginPage(self._driver)

    def add_backpack_one_to_cart(self):
        """
            Clicks on Add to Cart button for 'Sauce Labs Backpack' item.
        """
        self._click(p.add_to_cart_backpack_locator_one)
        return self

    def open_cart(self):
        """
            Clicks on Cart button.
            Returns a copy of CartPage class, allowing to use its methods.
        """
        self._click(p.cart_store_button_locator)
        from saucedemo_framework.page_objects.cart_page import CartPage
        return CartPage(self._driver)

    def is_secondary_header_located(self):
        """
            Checks if secondary header for Store Page is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.header_secondary_container_products)

    def quick_logout(self):
        """
            Opens burger menu and clicks on logout button.
            Returns a copy of LoginPage class, allowing to use its methods
        """
        self.open_burger_menu()._logout()
        from saucedemo_framework.page_objects.login_page import LoginPage
        return LoginPage(self._driver)
