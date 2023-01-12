import requests


class BaseAPI:
    def __init__(self, env):
        self.__base_url = env.base_url
        self._headers = {'Content-Type': 'application/json'}
        self.__request = requests

    def _get(self, url, headers=None, params=None):
        """
            A method for GET request.
            Takes url for API, headers and parameters.
        """
        if headers is None:
            headers = self._headers
        responses = self.__request.get(f'{self.__base_url}/{url}', params=params, headers=headers)
        return responses

    def _post(self, url, body=None, headers=None, params=None):
        """
            A method for POST request.
            Takes url for API, body, headers and parameters.
        """
        if headers is None:
            headers = self._headers
        response = self.__request.post(f'{self.__base_url}/{url}', json=body, headers=headers, params=params)
        return response

    def _delete(self, url, headers=None, params=None):
        """
            A method for DELETE request.
            Takes url for API, headers and parameters.
        """
        if headers is None:
            headers = self._headers
        response = self.__request.delete(f'{self.__base_url}/{url}', params=params, headers=headers)
        return response

    def _put(self, url, body=None, headers=None, params=None):
        """
            A method for PUT request.
            Takes url for API, body, headers and parameters.
        """
        if headers is None:
            headers = self._headers
        response = self.__request.put(f'{self.__base_url}/{url}', json=body, headers=headers, params=params)
        return response

    def _patch(self, url, body=None, headers=None, params=None):
        """
            A method for PATCH request.
            Takes url for API, body, headers and parameters.
        """
        if headers is None:
            headers = self._headers
        response = self.__request.patch(f'{self.__base_url}/{url}', json=body, headers=headers, params=params)
        return response
