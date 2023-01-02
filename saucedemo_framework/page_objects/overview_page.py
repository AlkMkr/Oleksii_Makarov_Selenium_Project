from saucedemo_framework.utilities.web_ui.base_page import BasePage
from saucedemo_framework.locators import locators as p


class OverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_overview_header_title_visible(self) -> bool:
        """
            Checks if Overview Page secondary header is displayed.
            Returns True or False.
        """
        return self._is_displayed(p.overview_header)

    def cancel_overview(self):
        """
            Clicks on Cancel button on Overview page.
            Returns a page object StorePage, allowing to use its methods.
        """
        self._click(p.overview_cancel_button)
        from saucedemo_framework.page_objects.store_page import StorePage
        return StorePage(self._driver)

    def finish_overview(self):
        """
            Clicks on Finish Overview button.
            Returns a page object CompletePage, allowing to use its methods.
        """
        self._click(p.overview_finish_button)
        from saucedemo_framework.page_objects.complete_page import CompletePage
        return CompletePage(self._driver)

    def _open_burger_menu(self):
        """
            Opens Burger menu.
        """
        self._click(p.burger_menu_button_locator)
        return self

    def _logout(self):
        """
            Clicks on Logout button in burger menu.
        """
        self._click(p.logout_button_locator)
        return self

    def fast_logout(self):
        """
            Opens Burger menu and clicks on logout button.
            Returns a page object LoginPage, allowing to use its methods.
        """
        self._open_burger_menu()._logout()
        from saucedemo_framework.page_objects.login_page import LoginPage
        return LoginPage(self._driver)
