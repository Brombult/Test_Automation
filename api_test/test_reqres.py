"""Example API test suite using 'requests' library"""
import requests

BASE_URL = 'https://reqres.in/api/'
USER_ID = '2'
NON_EXISTENT_USER_ID = '1232345'
EMAIL = 'johndoe@company.com'
PASSWORD = 'MyPassword'


def test_get_user_list():
    page = 'page=1'
    first_name = 'George'
    last_name = 'Bluth'
    r = requests.get(BASE_URL + 'users', params=page, timeout=2)
    assert r.ok
    total_pages = r.json()['total_pages']
    assert total_pages == 4
    data = r.json()['data']
    assert data[0]['first_name'] == first_name
    assert data[0]['last_name'] == last_name


def test_get_single_user():
    first_name = 'Janet'
    last_name = 'Weaver'
    r = requests.get(BASE_URL + 'users/' + USER_ID, timeout=2)
    assert r.ok
    data = r.json()['data']
    assert data['first_name'] == first_name
    assert data['last_name'] == last_name


def test_get_nonexistent_user():
    r = requests.get(BASE_URL + 'users/' + NON_EXISTENT_USER_ID, timeout=2)
    assert r.status_code == 404


def test_post_create_user():
    first_name = 'Ivan'
    last_name = 'Petrov'
    post_data = {'first_name': first_name,
                 'last_name': last_name, }
    r = requests.post(BASE_URL + 'users', data=post_data, timeout=2)
    assert r.status_code == 201
    assert first_name in r.text and last_name in r.text


def test_put_update_user():
    new_first_name = 'John'
    new_last_name = 'Doe'
    new_name = {'first_name': new_first_name,
                'last_name': new_last_name, }
    r = requests.put(BASE_URL + 'users/' + USER_ID, data=new_name, timeout=2)
    assert r.status_code == 200
    assert new_first_name in r.text and new_last_name in r.text


def test_delete_user():
    r = requests.delete(BASE_URL + 'users/' + USER_ID)
    assert r.status_code == 204


def test_post_register_user():
    post_data = {'email': EMAIL,
                 'password': PASSWORD}
    r = requests.post(BASE_URL + 'register', data=post_data, timeout=2)
    assert r.status_code == 201
    assert 'token' in r.text


def test_post_register_user_without_email():
    post_data = {'password': PASSWORD}
    r = requests.post(BASE_URL + 'register', data=post_data, timeout=2)
    assert r.status_code == 400
    assert 'Missing email or username' in r.text


def test_post_register_user_without_password():
    post_data = {'email': EMAIL}
    r = requests.post(BASE_URL + 'register', data=post_data, timeout=2)
    assert r.status_code == 400
    assert 'Missing password' in r.text


def test_post_login_successfully():
    post_data = {'email': EMAIL,
                 'password': PASSWORD}
    r = requests.post(BASE_URL + 'login', data=post_data, timeout=2)
    assert r.status_code == 200
    assert 'token' in r.text


def test_post_login_without_email():
    post_data = {'password': PASSWORD}
    r = requests.post(BASE_URL + 'login', data=post_data, timeout=2)
    assert r.status_code == 400
    assert 'Missing email or username' in r.text


def test_post_login_without_password():
    post_data = {'email': EMAIL}
    r = requests.post(BASE_URL + 'login', data=post_data, timeout=2)
    assert r.status_code == 400
    assert 'Missing password' in r.text


def test_get_timeout_expired():
    try:
        r = requests.get(BASE_URL + 'users/' + USER_ID, params='delay=5', timeout=2)
    except requests.exceptions.Timeout:
        return True
