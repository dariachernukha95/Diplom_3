from faker import Faker
import allure
import requests

from data import base_url, create_user_endpoint, delete_user_endpoint


class UserMethods:
    @allure.step('Создание пользователя через POST-запрос.')
    def create_user(self, payload):
        method_url = f"{base_url}{create_user_endpoint}"
        response = requests.post(url = method_url, data = payload)
        return response

    @allure.step('Удаление пользователя через DELETE-запрос.')
    def delete_user(self, access_token):
        method_url = f"{base_url}{delete_user_endpoint}"
        headers = {"authorization": access_token}
        response = requests.delete(url = method_url, headers = headers)
        return response

def generate_email():
    faker = Faker()
    email = faker.email()
    return email

def generate_password():
    faker = Faker()
    password = faker.password()
    return password

def generate_name():
    faker = Faker()
    name = faker.user_name()
    return name

@allure.step('Генерация тела запроса со всеми параметрами для создания пользователя.')
def generate_full_data_for_user_creation():
    payload = {"email": generate_email(),
               "password": generate_password(),
               "name": generate_name()}
    return payload

@allure.step('Регистрация пользователя и сохранение его данных.')
def create_new_user_and_return_user_data():
    email_password = {}
    payload = generate_full_data_for_user_creation()
    user_methods = UserMethods()
    response = user_methods.create_user(payload)
    access_token = response.json()["accessToken"]
    if response.status_code == 200:
        email_password["email"] = payload["email"]
        email_password["password"] = payload["password"]
    return email_password, access_token