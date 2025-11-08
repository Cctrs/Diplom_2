from datasets import *
import requests
import pytest
import allure
import urls

class TestChangeUserData:

    @allure.title('Проверка возможности изменения данных авторизованного пользователя')
    @pytest.mark.parametrize('update_params, expected_result', update_user_info)
    def test_update_user_info_authorized_success(self, create_user, delete_user, update_params, expected_result):

        access_token = create_user["response"].json()["accessToken"]

        payload = update_params
        headers = {"Authorization": access_token}
        response = requests.patch(urls.user_info_url, headers=headers, data=payload)
        response_body_text = response.json()

        assert response.status_code == 200
        assert response_body_text["success"] == True
        assert response_body_text["user"]["email"] == expected_result["email"]
        assert response_body_text["user"]["name"] == expected_result["name"]

        delete_user(access_token)

    
    @allure.title('Проверка возможности изменения данных неавторизованного пользователя')
    @pytest.mark.parametrize('update_params', update_user_info_without_authorization)
    def test_update_user_info_unauthorized_returns_error(self, create_user, delete_user, update_params):

        access_token = create_user["response"].json()["accessToken"]

        payload = update_params
        response = requests.patch(urls.user_info_url, data=payload)
        response_body_text = response.json()

        assert response.status_code == 401
        assert response_body_text["success"] == False
        assert response_body_text["message"] == authorization_error_message

        delete_user(access_token)