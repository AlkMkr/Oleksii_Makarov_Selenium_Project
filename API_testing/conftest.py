import json

import pytest

from API_testing.CONSTANTS import ROOT_DIR
from API_testing.config.config import Config
from API_testing.data.person_data import Person


@pytest.fixture()
def env():
    """
        Reads data from json config.
    """
    with open(f'{ROOT_DIR}/config/configuration.json') as file:
        env_dict = json.loads(file.read())
    return Config(**env_dict)


@pytest.fixture()
def created_person(env):
    """
        Creates an instance of Person class for comparison.
    """
    return Person(env.first_name1, env.last_name1, env.email1)
