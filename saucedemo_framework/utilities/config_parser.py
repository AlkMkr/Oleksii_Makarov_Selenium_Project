import configparser

from saucedemo_framework.CONSTANTS import ROOT_DIR

config = configparser.RawConfigParser()
config.read(f'{ROOT_DIR}\configurations\configuration.ini')


class ReadConfig:
    @staticmethod
    def get_base_url() -> str:
        """
            Get site url.
        """
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_login() -> str:
        """
            Get login data for user.
        """
        return config.get('user_info', 'login')

    @staticmethod
    def get_password() -> str:
        """
            Get password data for user.
        """
        return config.get('user_info', 'password')

    @staticmethod
    def get_driver_id() -> int:
        """
            Get driver ID for browser. (1-Chrome, 2-Firefox, 3-Edge, else - Chrome).
        """
        return config.getint('browser', 'browser_id')

    @staticmethod
    def get_headless() -> bool:
        """
            Get Headless parameter for running browser in Headless-mode(i.e. without visual output)
        """
        return config.getboolean('browser', 'is_headless')

    @staticmethod
    def get_first_name() -> str:
        """
            Get first name data for Checkout Page fields.
        """
        return config.get('user_info', 'first_name')

    @staticmethod
    def get_last_name() -> str:
        """
            Get last name data for Checkout Page fields.
        """
        return config.get('user_info', 'second_name')

    @staticmethod
    def get_postal_code() -> str:
        """
            Get postal code data for Checkout Page fields.
        """
        return config.get('user_info', 'postal_code')
