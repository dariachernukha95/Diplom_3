import allure
from data import email, password, personal_account_url, order_history_url, login_url
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:
    @allure.title('Проверка перехода в лк пользователя по кнопке «Личный кабинет»')
    def test_go_to_personal_account_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_into_account_button()
        login_page = LoginPage(driver)
        login_page.fill_input_field_email(email)
        login_page.fill_input_field_password(password)
        login_page.click_login_button()
        main_page.find_make_order_button()
        main_page.click_personal_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.find_description_of_profile_page()
        assert driver.current_url == personal_account_url

    @allure.title('Проверка перехода в раздел истории заказов из личного кабинета')
    def test_go_to_order_history_page(self, driver, log_in):
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_order_history_link()
        assert driver.current_url == order_history_url

    @allure.title('Проверка выхода из аккаунта из личного кабинета')
    def test_exit_from_personal_account(self, driver,log_in):
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_exit_button()
        login_page = LoginPage(driver)
        login_page.find_login_header()
        assert driver.current_url == login_url

