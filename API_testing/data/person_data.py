import json


class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @classmethod
    def from_json(cls, **kwargs):
        """
            A class method that takes json of response and returns dict of a class with three keys:
            "first_name", "last_name", "email"
        """
        return cls(kwargs["data"]['first_name'], kwargs["data"]['last_name'], kwargs["data"]['email'])

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_dict(self):
        """
            Returns a class a a dict.
        """
        return self.__dict__
