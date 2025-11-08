import pytest
from datasets import *
import urls
import requests

@pytest.fixture
def create_user():
    payload = creds_for_registration
    response = requests.post(urls.registration_url, data=payload)
    return {
        "response" : response
    }


@pytest.fixture
def login_user():
    
    def _login():
        payload = creds_for_registration
        response = requests.post(urls.authorization_url, data=payload)
        return {
        "response" : response
        }
    return _login


@pytest.fixture
def delete_user():
    
    def _delete(access_token):
        headers = {"Authorization": access_token}
        response = requests.delete(urls.user_info_url, headers=headers)
        return response
    return _delete


@pytest.fixture
def create_order():

    def _create(access_token):
        headers = {"Authorization": access_token}
        payload = order_with_correct_ingredients
        response = requests.post(urls.order_url, headers=headers, data = payload)
        return response
    return _create
