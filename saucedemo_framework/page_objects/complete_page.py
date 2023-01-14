from saucedemo_framework.page_objects.burger_menu import BurgerMenu
from saucedemo_framework.utilities.decorator import auto_add_step
from saucedemo_framework.utilities.web_ui.base_page import BasePage
from saucedemo_framework.locators import locators as p


@auto_add_step
class CompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def complete_back_home(self):
        """
            Clicks on Back Home button.
            Returns a page object StorePage, allowing to use its methods.
        """
        self._click(p.complete_page_back)
        from saucedemo_framework.page_objects.store_page import StorePage
        return StorePage(self._driver)

    def is_header_visible(self) -> bool:
        """
            Checks if secondary header of Complete Page is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.complete_header)

    def open_burger_menu(self) -> BurgerMenu:
        """
            CLicks on Burger Menu.
            Returns a page object BurgerMenu, allowing to use its methods.
        """
        self._click(p.burger_menu_button_locator)
        return BurgerMenu(self._driver)
