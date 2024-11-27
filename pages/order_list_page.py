from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage
import allure

class OrderListPage(BasePage):

    @allure.step('Находим заголовок Лента заказов')
    def find_order_list_header(self):
        self.find_element_with_wait(OrderListPageLocators.ORDER_LIST_HEADER)

    @allure.step('Нажимаем на 1-ую карточку заказа')
    def click_first_order_card(self):
        self.move_to_element_and_click(OrderListPageLocators.ORDER_CARD)

    @allure.step('Находим всплывающее окно с деталями заказа')
    def find_order_window(self):
        return self.find_element_with_wait(OrderListPageLocators.ORDER_WINDOW)

    @allure.step('Получаем список заказов в работе')
    def get_order_list_in_work(self):
        return self.get_text_from_element(OrderListPageLocators.ORDER_LIST_IN_WORK)

    @allure.step('Получаем идентификатор последнего заказа в истории')
    def get_last_order_in_order_list(self):
        return self.get_text_from_element(OrderListPageLocators.LAST_ORDER_ID)

    @allure.step('Получаем значение счетчика выполненных за все время заказов')
    def get_all_orders_value(self):
        return self.get_text_from_element(OrderListPageLocators.ALL_ORDERS_COUNTER)

    @allure.step('Получаем значение счетчика выполненных за сегодня заказов')
    def get_today_orders_value(self):
        return self.get_text_from_element(OrderListPageLocators.TODAY_ORDERS_COUNTER)