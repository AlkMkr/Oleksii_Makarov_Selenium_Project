from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 3)

    def _wait_until_element_located(self, locator: str):
        """
            Takes locator as a parameter.
            Return an element based on its locator, when driver locates it on the HTML DOM.
            If it can't return element in 5 seconds returns TimeoutException.
        """
        return self.__wait.until(EC.presence_of_element_located(locator))

    def _wait_until_element_clickable(self, locator: str):
        """
            Takes locator as a parameter.
            Return an element based on its locator, when driver recognize that it's visible and clickable on webpage.
            If it can't return element in 5 seconds returns TimeoutException.
        """
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def _wait_until_element_visible(self, locator):
        """
            Takes locator as a parameter.
            Return an element based on its locator, when driver recognizes that it's visible on webpage.
            If it can't return element in 5 seconds returns TimeoutException.
        """
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def _send_keys(self, locator: str, value: str, is_clear=True):
        """
            Takes three parameters. Locator, value and is_clear.
            Waits until element is located.
            Then if is_clear equal False, it clears input field of element.
            Then parameter value into the field of element.
        """
        element = self._wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def _click(self, locator: str):
        """
            Takes locator as a parameter.
            Waits until element is clickable.
            Clicks on the element.
        """
        element = self._wait_until_element_clickable(locator)
        element.click()

    def _is_displayed(self, locator: str) -> bool:
        """
            Takes one parameter: locator.
            If driver can recognize that element is visible, return True.
            Otherwise, return False.
        """
        try:
            self._wait_until_element_visible(locator)
            return True
        except TimeoutException:
            return False
