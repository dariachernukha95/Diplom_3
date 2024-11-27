from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):

    @allure.step('Нажимаем на кнопку Восстановить пароль')
    def click_recover_password_button(self):
        self.move_to_element_and_click(LoginPageLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step('Заполняем поле Email на странице входа в аккаунт')
    def fill_input_field_email(self, email):
        self.fill_input_field(LoginPageLocators.INPUT_FIELD_EMAIL, email)

    @allure.step('Заполняем поле Email на странице входа в аккаунт')
    def fill_input_field_password(self, password):
        self.fill_input_field(LoginPageLocators.INPUT_FIELD_PASSWORD, password)

    @allure.step('Нажимаем на кнопку Войти')
    def click_login_button(self):
        self.move_to_element_and_click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Находим заголовок Вход')
    def find_login_header(self):
        self.find_element_with_wait(LoginPageLocators.LOGIN_HEADER)
