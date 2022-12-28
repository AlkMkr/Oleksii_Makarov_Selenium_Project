import configparser

from saucedemo_framework.CONSTANTS import ROOT_DIR

config = configparser.RawConfigParser()
config.read(f'{ROOT_DIR}\configurations\configuration.ini')


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_login():
        return config.get('user_info', 'login')

    @staticmethod
    def get_password():
        return config.get('user_info', 'password')

    @staticmethod
    def get_driver_id():
        return config.get('browser', 'browser_id')

    @staticmethod
    def get_headless():
        return config.getboolean('browser', 'is_headless')

    @staticmethod
    def get_first_name():
        return config.get('user_info', 'first_name')

    @staticmethod
    def get_last_name():
        return config.get('user_info', 'second_name')

    @staticmethod
    def get_postal_code():
        return config.get('user_info', 'postal_code')
