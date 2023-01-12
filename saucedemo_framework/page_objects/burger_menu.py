import allure

from saucedemo_framework.utilities.decorator import auto_add_step
from saucedemo_framework.utilities.web_ui.base_page import BasePage
from saucedemo_framework.page_objects.login_page import LoginPage
from saucedemo_framework.locators import locators as p


@auto_add_step
class BurgerMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

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

    def logout(self) -> LoginPage:
        """
            Clicks on Logout button in already opened burger menu.
            Returns a page object LoginPage, allowing to use its methods
        """
        self._click(p.logout_button_locator)
        return LoginPage(self._driver)
