from urls import *
import requests
import allure
from datasets import *

class TestGetUserOrders:
    
    @allure.title('Проверка возможности получения списка заказов авторизованного пользователя')
    def test_get_user_orders_with_authorization_success(self, create_user, create_order, delete_user):

        access_token = create_user["response"].json()["accessToken"]

        create_order(access_token)

        headers = {"Authorization": access_token}
        response = requests.get(order_url, headers=headers)
        response_body_text = response.json()

        assert response.status_code == 200
        assert response_body_text["success"] == True
        assert isinstance(response_body_text["orders"][0]["_id"], str)
        assert isinstance(response_body_text["orders"][0]["number"], int)
        assert response_body_text["orders"][0]["name"] == "Флюоресцентный spicy бургер"

        delete_user(access_token)


    @allure.title('Проверка невозможности получения списка заказов неавторизованного пользователя')
    def test_get_user_orders_without_authorization_returns_error(self, create_user, create_order, delete_user):

        access_token = create_user["response"].json()["accessToken"]

        create_order(access_token)

        response = requests.get(order_url)
        response_body_text = response.json()

        assert response.status_code == 401
        assert response_body_text["success"] == False
        assert response_body_text["message"] == authorization_error_message

        delete_user(access_token)