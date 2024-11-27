from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage
import allure

class PersonalAccountPage(BasePage):

    @allure.step('Находим на странице описание профиля')
    def find_description_of_profile_page(self):
        self.find_element_with_wait(PersonalAccountPageLocators.DESCRIPTION_OF_PROFILE_PAGE)

    @allure.step('Переходим в раздел История заказов')
    def click_order_history_link(self):
        self.move_to_element_and_click(PersonalAccountPageLocators.ORDER_HISTORY_LINK)

    @allure.step('Нажимаем на кнопку Выход')
    def click_exit_button(self):
        self.move_to_element_and_click(PersonalAccountPageLocators.EXIT_BUTTON)
