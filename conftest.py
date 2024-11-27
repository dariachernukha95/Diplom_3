import pytest
from selenium import webdriver
import data
from data import base_url
from helpers import create_new_user_and_return_user_data, UserMethods
from pages.login_page import LoginPage
from pages.main_page import MainPage

# Переназначение глобальной переменной driver_name добавлено для использования метода drag_and_drop_element
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        data.driver_name = "chrome"
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        data.driver_name = "firefox"
    driver.get(base_url)
    yield driver
    driver.quit()

@pytest.fixture
def log_in(driver, email_password):
    main_page = MainPage(driver)
    main_page.click_login_into_account_button()
    login_page = LoginPage(driver)
    login_page.fill_input_field_email(email_password['email'])
    login_page.fill_input_field_password(email_password['password'])
    login_page.click_login_button()
    main_page.find_make_order_button()

@pytest.fixture
def email_password():
    email_password, access_token = create_new_user_and_return_user_data()
    yield email_password
    user_methods = UserMethods()
    user_methods.delete_user(access_token)