from datasets import *
from urls import *
import requests
import allure

class TestCreateOrder:
    
    @allure.title('Проверка возможности создания заказа авторизованным пользователем')
    def test_create_order_with_authorization_success(self, create_user, delete_user):

        access_token = create_user["response"].json()["accessToken"]

        payload = order_with_correct_ingredients
        headers = {"Authorization": access_token}
        response = requests.post(order_url, headers=headers, json=payload)
        response_body_text = response.json()

        assert response.status_code == 200
        assert response_body_text["success"] == True
        assert response_body_text["name"] == "Флюоресцентный spicy бургер"
        assert isinstance(response_body_text["order"]["_id"], str)
        assert isinstance(response_body_text["order"]["number"], int)
        assert response_body_text["order"]["owner"]["name"] == "CosmoCaactusBurger10000"

        delete_user(access_token)

    
    @allure.title('Проверка возможности создания заказа неавторизованным пользователем')
    def test_create_order_without_authorization_success(self):

        payload = order_with_correct_ingredients
        response = requests.post(order_url, json=payload)
        response_body_text = response.json()

        assert response.status_code == 200
        assert response_body_text["success"] == True
        assert response_body_text["name"] == "Флюоресцентный spicy бургер"


    @allure.title('Проверка возможности создания заказа c ингридиентами')
    def test_create_order_with_ingredients_success(self, create_user, delete_user):

        access_token = create_user["response"].json()["accessToken"]

        payload = order_with_correct_ingredients
        headers = {"Authorization": access_token}
        response = requests.post(order_url, headers=headers, json=payload)
        response_body_text = response.json()

        assert response.status_code == 200
        assert response_body_text["success"] == True
        assert response_body_text["name"] == "Флюоресцентный spicy бургер"
        assert response_body_text["order"]["ingredients"][0]["name"] == "Флюоресцентная булка R2-D3"
        assert response_body_text["order"]["ingredients"][1]["name"] == "Соус Spicy-X"
        
        delete_user(access_token)


    @allure.title('Проверка невозможности создания заказа без ингридиентов')
    def test_create_order_without_ingredients_returns_error(self, create_user, delete_user):

        access_token = create_user["response"].json()["accessToken"]

        payload = order_without_ingredients
        headers = {"Authorization": access_token}
        response = requests.post(order_url, headers=headers, json=payload)
        response_body_text = response.json()

        assert response.status_code == 400
        assert response_body_text["success"] == False
        assert response_body_text["message"] == wrong_ingredient_error_message

        delete_user(access_token)


    @allure.title('Проверка невозможности создания заказа c неверным хэшем ингридиентов')
    def test_create_order_with_wrong_ingredients_hash_returns_error(self, create_user, delete_user):

        access_token = create_user["response"].json()["accessToken"]

        payload = ingredients_with_wrong_hash
        headers = {"Authorization": access_token}
        response = requests.post(order_url, headers=headers, json=payload)

        assert response.status_code == 500

        delete_user(access_token)