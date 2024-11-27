from locators.recover_password_page_locators import RecoverPasswordPageLocators
from pages.base_page import BasePage
import allure

class RecoverPasswordPage(BasePage):

    @allure.step('Заполняем поле Email на странице восстановления пароля')
    def fill_input_field_email(self, email):
        self.fill_input_field(RecoverPasswordPageLocators.EMAIL_INPUT_FIELD, email)

    @allure.step('Нажимаем на кнопку Восстановить')
    def click_recover_button(self):
        self.move_to_element_and_click(RecoverPasswordPageLocators.RECOVER_BUTTON)

    @allure.step('Находим на странице поле ввода Пароль')
    def find_password_input_field(self):
        self.find_element_with_wait(RecoverPasswordPageLocators.PASSWORD_INPUT_FIELD_HIDDEN)

    @allure.step('Находим на странице заголовок формы Восстановление пароля')
    def find_recover_password_header(self):
        self.find_element_with_wait(RecoverPasswordPageLocators.RECOVER_PASSWORD_HEADER)

    @allure.step('Нажимаем на кнопку показать/скрыть пароль в поле ввода пароля')
    def click_show_password_button(self):
        self.move_to_element_and_click(RecoverPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Находим на странице поле ввода с открытым паролем')
    def find_visible_password_input_field(self):
        return self.find_element_with_wait(RecoverPasswordPageLocators.PASSWORD_INPUT_FIELD_VISIBLE)

    @allure.step('Находим активное состояние поля ввода')
    def find_active_status_of_password_input_field(self):
        return self.find_element_with_wait(RecoverPasswordPageLocators.ACTIVE_STATUS_OF_INPUT_FIELD)