from saucedemo_framework.utilities.web_ui.base_page import BasePage
from saucedemo_framework.locators import locators as p
from saucedemo_framework.page_objects.store_page import StorePage
from saucedemo_framework.page_objects.checkout_page import CheckoutPage
from saucedemo_framework.page_objects.login_page import LoginPage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_there_items_in_cart(self) -> bool:
        """
            Checks if there's any item in cart with locator //div[@class='cart_item'] present.
            Returns True or False
        """
        return self._is_displayed(p.item_in_cart_locator)

    def is_remove_button_displayed(self) -> bool:
        """
            Checks if the 'remove' button in cart for item 'Sauce Labs Backpack' is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.remove_saucelab_backpack_cart_locator)

    def is_item_and_remove_present(self) -> bool:
        """
            Checks if there's any item in cart with locator //div[@class='cart_item'] present.
            And checks if the 'remove' button in cart for item 'Sauce Labs Backpack' is displayed.
            Return True or False.
        """
        return all([self.is_there_items_in_cart(), self.is_remove_button_displayed()])

    def click_remove_button(self):
        """
            Clicks on 'remove' button in cart for item 'Sauce Labs Backpack'.
        """
        self._click(p.remove_saucelab_backpack_cart_locator)
        return self

    def is_cart_header_displayed(self) -> bool:
        """
            Checks if the secondary header with writing 'YOUR CART' is displayed in cart page.
            Returns True or False.
        """
        return self._is_displayed(p.header_secondary_container_cart)

    def continue_shopping(self) -> StorePage:
        """
            Clicks on 'Continue shopping' button on cart page.
            Returns a page object of StorePage, allowing to use its methods in test.
        """
        self._click(p.cart_button_continue_shopping)
        from saucedemo_framework.page_objects.store_page import StorePage
        return StorePage(self._driver)

    def click_checkout(self) -> CheckoutPage:
        """
            Clicks on checkout button in cart page.
            Returns a page object CheckoutPage, allowing to use its methods.
        """
        self._click(p.cart_checkout_button)
        from saucedemo_framework.page_objects.checkout_page import CheckoutPage
        return CheckoutPage(self._driver)

    def open_burger_menu(self):
        """
            Opens burger menu.
        """
        self._click(p.burger_menu_button_locator)
        return self

    def _is_burger_menu_located(self) -> bool:
        """
            Checks if burger menu is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.burger_menu_locator)

    def _is_burger_menu_about_displayed(self) -> bool:
        """
            Checks if About button in burger menu is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.burger_about_button_locator)

    def _is_burger_menu_reset_displayed(self) -> bool:
        """
            Checks if Reset button in burger menu is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.burger_reset_button_locator)

    def _is_burger_menu_all_items_displayed(self) -> bool:
        """
            Checks if All Items button in burger menu is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.burger_all_items_button_locator)

    def _is_burger_menu_logout_displayed(self) -> bool:
        """
            Checks if Logout button in burger menu is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.logout_button_locator)

    def _is_burger_menu_close_button_located(self) -> bool:
        """
            Checks if Close(x) button in burger menu is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.burger_menu_close_locator)

    def is_burger_menu_filled(self) -> bool:
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
        """
        self._click(p.logout_button_locator)
        return self

    def quick_logout(self) -> LoginPage:
        """
            Opens burger menu and clicks on logout button.
            Returns a page object LoginPage, allowing to use its methods
        """
        self.open_burger_menu()._logout()
        from saucedemo_framework.page_objects.login_page import LoginPage
        return LoginPage(self._driver)
