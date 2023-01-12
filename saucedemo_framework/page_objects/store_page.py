from saucedemo_framework.locators import locators as p
from saucedemo_framework.page_objects.burger_menu import BurgerMenu
from saucedemo_framework.utilities.decorator import auto_add_step
from saucedemo_framework.utilities.web_ui.base_page import BasePage


@auto_add_step
class StorePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_burger_menu(self) -> BurgerMenu:
        """
            CLicks on Burger Menu.
            Returns a page object BurgerMenu, allowing to use its methods.
        """
        self._click(p.burger_menu_button_locator)
        return BurgerMenu(self._driver)

    def add_backpack_one_to_cart(self):
        """
            Clicks on Add to Cart button for 'Sauce Labs Backpack' item.
        """
        self._click(p.add_to_cart_backpack_locator_one)
        return self

    def open_cart(self):
        """
            Clicks on Cart button.
            Returns page object CartPage, allowing to use its methods.
        """
        self._click(p.cart_store_button_locator)
        from saucedemo_framework.page_objects.cart_page import CartPage
        return CartPage(self._driver)

    def is_secondary_header_located(self) -> bool:
        """
            Checks if secondary header for Store Page is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.header_secondary_container_products)
