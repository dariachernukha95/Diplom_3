import allure
from data import recover_password_url, reset_password_url, email
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.recover_password_page import RecoverPasswordPage


class TestRecoverPassword:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_forgot_password_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_into_account_button()
        login_page = LoginPage(driver)
        login_page.click_recover_password_button()
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.find_recover_password_header()
        assert driver.current_url == recover_password_url

    @allure.title('Проверка перехода на страницу сброса пароля ')
    @allure.description('Проверяем, что при вводе почты и клике по кнопке «Восстановить» происходит переход на страницу сброса пароля.')
    def test_go_to_reset_password_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_into_account_button()
        login_page = LoginPage(driver)
        login_page.click_recover_password_button()
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.fill_input_field_email('dchernukha@mail.ru')
        recover_password_page.click_recover_button()
        recover_password_page.find_password_input_field()
        assert driver.current_url == reset_password_url

    @allure.title('Проверка клика по кнопке показать/скрыть пароль')
    @allure.description('Проверяем, что при клике по кнопке показать пароль поле ввода становится активным, и пароль становится видимым.')
    def test_show_password_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_into_account_button()
        login_page = LoginPage(driver)
        login_page.click_recover_password_button()
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.fill_input_field_email(email)
        recover_password_page.click_recover_button()
        recover_password_page.click_show_password_button()
        assert (recover_password_page.find_visible_password_input_field() and recover_password_page.find_active_status_of_password_input_field())
