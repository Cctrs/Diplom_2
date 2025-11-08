from datasets import *
import requests
import pytest
import allure
import urls

class TestCreateUser:
    
    @allure.title('Проверка возможности создания нового пользователя')
    def test_create_new_user_success(self, create_user, delete_user):

        create_user_response = create_user["response"]
        response_body_text = create_user_response.json()

        assert create_user_response.status_code == 200
        assert response_body_text["success"] == True
        assert response_body_text["user"]["email"] == creds_for_registration["email"]
        assert response_body_text["user"]["name"] == creds_for_registration["name"]
        assert response_body_text["accessToken"].startswith("Bearer ")
        assert "refreshToken" in response_body_text

        access_token = response_body_text["accessToken"]
        delete_user(access_token)


    @allure.title('Проверка невозможности создания двух одинаковых пользователей под логином, который уже есть')
    def test_create_two_equal_users_returns_error(self, create_user, delete_user):
        payload = creds_for_registration
        create_user_response = create_user["response"]
        create_user_response_body_text = create_user_response.json()
        second_response = requests.post(urls.registration_url, data=payload)
        response_body_text = second_response.json()

        assert second_response.status_code == 403
        assert response_body_text['success'] == False
        assert response_body_text['message'] == user_already_exists_message

        access_token = create_user_response_body_text["accessToken"]
        delete_user(access_token)

  
    @allure.title('Проверка невозможности создания нового пользователя без передачи обязательных полей')
    @pytest.mark.parametrize('empty_params', empty_required_params)
    def test_create_user_without_required_params_returns_error(self, empty_params):

        payload = empty_params
        response = requests.post(urls.registration_url, data=payload)
        response_body_text = response.json()

        assert response.status_code == 403
        assert response_body_text['message'] == empty_required_fields_message