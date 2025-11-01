from datasets import *
from urls import *
import requests
import pytest
import allure

class TestLoginUser:
    
    @allure.title('Проверка возможности логина существующим пользователем')
    def test_login_user_success(self, create_user, login_user, delete_user):

        access_token = create_user["response"].json()["accessToken"]

        response = login_user()["response"]
        response_body_text = response.json()

        assert response.status_code == 200
        assert response_body_text["success"] == True
        assert response_body_text["user"]["email"] == creds_for_registration["email"]
        assert response_body_text["user"]["name"] == creds_for_registration["name"]
        assert response_body_text["accessToken"].startswith("Bearer ")
        assert "refreshToken" in response_body_text

        delete_user(access_token)

    
    @allure.title('Проверка невозможности залогиниться с неправильным логином или паролем')
    @pytest.mark.parametrize('wrong_params_for_login', wrong_creds_for_login)
    def test_wrong_creds_returns_login_error(self, create_user, delete_user, wrong_params_for_login):

        access_token = create_user["response"].json()["accessToken"]
        
        payload = wrong_params_for_login
        response = requests.post(authorization_url, data=payload)
        response_body_text = response.json()

        assert response.status_code == 401
        assert response_body_text["success"] == False
        assert response_body_text['message'] == wrong_creds_error_message

        delete_user(access_token)