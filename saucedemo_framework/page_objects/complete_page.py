from saucedemo_framework.utilities.web_ui.base_page import BasePage
from saucedemo_framework.locators import locators as p


class CompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def complete_back_home(self):
        """
            Clicks on Back Home button.
            Returns a copy of StorePage class, allowing to use its methods.
        """
        self._click(p.complete_page_back)
        from saucedemo_framework.page_objects.store_page import StorePage
        return StorePage(self._driver)

    def is_header_visible(self):
        """
            Checks if secondary header of Complete Page is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.complete_header)

    def _open_burger_menu(self):
        """
            Opens Burger menu.
        """
        self._click(p.burger_menu_button_locator)
        return self

    def _logout(self):
        """
            Clicks on Logout button in Burger menu.
        """
        self._click(p.logout_button_locator)
        return self

    def fast_logout(self):
        """
            Opens Burger menu and clicks on Logout Button.
            Returns a copy of LoginPage class, allowing to use its methods.
        """
        self._open_burger_menu()._logout()
        from saucedemo_framework.page_objects.login_page import LoginPage
        return LoginPage(self._driver)
