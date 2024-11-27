from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure

class MainPage(BasePage):

    @allure.step('Нажимаем на кнопку Войти в аккаунт')
    def click_login_into_account_button(self):
        self.move_to_element_and_click(MainPageLocators.LOGIN_INTO_ACCOUNT_BUTTON)

    @allure.step('Нажимаем на кнопку Личный кабинет')
    def click_personal_account_button(self):
        self.move_to_element_and_click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Находим кнопку Оформить заказ')
    def find_make_order_button(self):
        self.find_element_with_wait(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Нажимаем на кнопку Конструктор')
    def click_constructor_button(self):
        self.move_to_element_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Находим заголовок Соберите бургер')
    def find_make_burger_header(self):
        self.find_element_with_wait(MainPageLocators.MAKE_BURGER_HEADER)

    @allure.step('Нажимаем на кнопку Лента заказов')
    def click_order_list_button(self):
        self.move_to_element_and_click(MainPageLocators.ORDER_LIST_BUTTON)

    @allure.step('Нажимаем на ингредиент Флюоресцентная булка')
    def click_fluorescent_bun(self):
        self.move_to_element_and_click(MainPageLocators.FLUORESCENT_BUN)

    @allure.step('Перетягивание булочки')
    def drag_and_drop_bun(self):
        self.drag_and_drop_element(MainPageLocators.FLUORESCENT_BUN, MainPageLocators.FIELD_FOR_BUN_UP)

    @allure.step('Получение значения счетчика булочки')
    def get_bun_counter_value(self):
        return self.get_text_from_element(MainPageLocators.BUN_COUNTER)

    @allure.step('Нажимаем на кнопку Оформить заказ')
    def click_make_order_button(self):
        self.move_to_element_and_click(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Находим текст о подтверждении заказа во всплывающем окне')
    def find_order_confirmation(self):
        return self.find_element_with_wait(MainPageLocators.ORDER_TEXT)

    @allure.step('Получаем id созданного заказа')
    def get_order_id(self):
        return self.get_text_from_element(MainPageLocators.ORDER_ID)

    @allure.step('Находим элемент id созданного заказа')
    def find_order_id(self):
        return self.find_element_with_wait(MainPageLocators.ORDER_ID)

    @allure.step('Нажимаем на кнопку закрытия всплывающего окна заказа')
    def click_close_order_window_button(self):
        self.move_to_element_and_click(MainPageLocators.CLOSE_ORDER_WINDOW_BUTTON)


