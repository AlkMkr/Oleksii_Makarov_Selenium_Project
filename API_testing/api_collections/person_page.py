import json

from API_testing.utilities.base_api import BaseAPI
from saucedemo_framework.utilities.decorator import auto_add_step


@auto_add_step
class UserAPI(BaseAPI):

    def __init__(self, env):
        super().__init__(env)
        self.__user_url = 'api/users'
        self.__register = 'api/register'

    def get_user(self, person_id: int):
        """
            A method for GET request for https://reqres.in/api/users. Takes ID of user.
            Should return the user with this ID.
        """
        response = self._get(f'{self.__user_url}/{person_id}')
        return response

    def get_list_of_users(self, page: int):
        """
            A method for GET request for https://reqres.in/api/users?page=page. Takes page number.
            Should return the list of users.
        """
        response = self._get(f'{self.__user_url}?page={page}')
        return response

    def create_user(self, person_data: dict):
        """
            A method for POST request for https://reqres.in/api/users. Takes a dict as a body for the request.
        """
        json_data = json.dumps(person_data)
        response = self._post(url=f'{self.__user_url}', body=json_data,
                              headers={'Content-Type': 'text/html; charset=utf-8'})
        return response

    def delete_user(self, person_id: int):
        """
            A method for DELETE request for https://reqres.in/api/users. Takes and ID of user.
        """
        response = self._delete(url=f'{self.__user_url}/{person_id}')
        return response

    def put_user(self, person_id: int, person_data: dict):
        """
            A method for PUT request for https://reqres.in/api/users. Takes and ID of user and dict as a body of request.
        """
        response = self._put(url=f'{self.__user_url}/{person_id}', body=person_data)
        return response

    def patch_user(self, person_id: int, person_data: dict):
        """
            A method for PATCH request for https://reqres.in/api/users. Takes and ID of user and dict as a body of request.
        """
        response = self._patch(url=f'{self.__user_url}/{person_id}', body=person_data)
        return response

    def post_register(self, register_info: dict):
        """
            A method for POST request for https://reqres.in/api/register. Takes a dict as a body for the request.
        """
        response = self._post(url=f'{self.__register}', body=register_info,
                              headers={'Content-Type': 'text/html; charset=utf-8'})
        return response
