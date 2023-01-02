import configparser

from saucedemo_framework.CONSTANTS import ROOT_DIR

config = configparser.RawConfigParser()
config.read(f'{ROOT_DIR}\configurations\configuration.ini')


class ReadConfig:
    @staticmethod
    def get_base_url():
        """
            Get site url.
        """
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_login():
        """
            Get login data for user.
        """
        return config.get('user_info', 'login')

    @staticmethod
    def get_password():
        """
            Get password data for user.
        """
        return config.get('user_info', 'password')

    @staticmethod
    def get_driver_id():
        """
            Get driver ID for browser. (1-Chrome, 2-Firefox, 3-Edge).
        """
        return config.get('browser', 'browser_id')

    @staticmethod
    def get_headless():
        """
            Get Headless parameter for running browser in Headless-mode(i.e. without visual output)
        """
        return config.getboolean('browser', 'is_headless')

    @staticmethod
    def get_first_name():
        """
            Get first name data for Checkout Page fields.
        """
        return config.get('user_info', 'first_name')

    @staticmethod
    def get_last_name():
        """
            Get last name data for Checkout Page fields.
        """
        return config.get('user_info', 'second_name')

    @staticmethod
    def get_postal_code():
        """
            Get postal code data for Checkout Page fields.
        """
        return config.get('user_info', 'postal_code')
