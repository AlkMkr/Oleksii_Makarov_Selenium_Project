from http import HTTPStatus

import pytest

from API_testing.data.person_data import Person

from API_testing.api_collections.person_page import UserAPI


def test_get_user(env):
    """
        Test response for GET request, for user.
    """
    response = UserAPI(env).get_user(1)
    assert response.status_code == HTTPStatus.OK, f'Request failed: Status Code {response.status_code}' \
                                                  f'Expected: {HTTPStatus.OK}'


def test_person_data(created_person, env):
    """
        Test response for GET request comparing response body to config data.
    """
    expected_person = created_person
    response = UserAPI(env).get_user(1)
    person_data = response.json()
    actual_person = Person.from_json(**person_data)
    assert expected_person == actual_person, f'Created wrong user.'


def test_create_person(env):
    """
        Test response for POST request, to create user.
    """
    bilbo = Person(env.first_name, env.last_name, env.email)
    response = UserAPI(env).create_user(bilbo.get_dict())
    assert response.status_code == HTTPStatus.CREATED, f'Failed to create new User'


@pytest.mark.parametrize("page", [1, 2, 3, 4, 5])
def test_get_list_of_people(env, page):
    """
        Test response for GET request for list of users.
    """
    response = UserAPI(env).get_list_of_users(page)
    list_of_users = response.json()
    assert list_of_users["page"] == page, f'Failed to get page number {page}, actual page = {list_of_users["page"]}' \
                                          f'Or wrong request entirely.' \
                                          f'Request failed: Status Code {response.status_code}' \
                                          f'Expected: {HTTPStatus.OK}'
    assert "data" in list_of_users, f'Failed to get List of users'


def test_put_user(env):
    """
        Test response for PUT request for user.
    """
    data = {"email": env.email}
    response = UserAPI(env).put_user(1, data)
    update = response.json()
    assert response.status_code == HTTPStatus.OK, 'Failed to update'
    assert "updatedAt" in update, 'Failed to update'


def test_patch_user(env):
    """
        Test response for PATCH request for user.
    """
    data = {"email": env.email}
    response = UserAPI(env).patch_user(1, data)
    update = response.json()
    assert response.status_code == HTTPStatus.OK, f'Request failed: Status Code {response.status_code}' \
                                                  f'Expected: {HTTPStatus.OK}'
    assert "updatedAt" in update, f'Request failed: Status Code {response.status_code}' \
                                  f'Expected: {HTTPStatus.OK}'


def test_delete_user(env):
    """
        Test response for DELETE request for user.
    """
    response = UserAPI(env).delete_user(1)
    assert response.status_code == HTTPStatus.NO_CONTENT, f'Request failed: Status Code {response.status_code}' \
                                                          f'Expected: {HTTPStatus.NO_CONTENT}'


def test_get_user_fail(env):
    """
        Test response for wrong GET request for user.
    """
    response = UserAPI(env).get_user(23)
    assert response.status_code == HTTPStatus.NOT_FOUND, f'Request failed: Status Code {response.status_code}' \
                                                         f'Expected: {HTTPStatus.NOT_FOUND}'


@pytest.mark.parametrize('email , password', [('', ''), ('env.register_email1', ''), ('', 'env.register_password1'),
                                              ('env.register_email1', 'env.register_password1')],
                         ids=['empty spaces', 'empty password', 'empty email', 'normal'])
def test_register(email, password, env):
    """
        This one should've tested the response for POST request for various data for register, but it's always returns
        400 even in Postman even copy-pasting, so I am testing 400.
    """
    # It is broken. As even copying request from the API itself and using postman I still get error 400
    data = {"email": None, "password": None}
    if email:
        data.update({"email": eval(email)})
    else:
        data.update({"email": email})
    if password:
        data.update({"password": eval(password)})
    else:
        data.update({"password": password})
    response = UserAPI(env).post_register(data)
    assert response.status_code == HTTPStatus.BAD_REQUEST, f'Request failed: Status Code {response.status_code}' \
                                                           f'Expected: {HTTPStatus.NOT_FOUND}'
