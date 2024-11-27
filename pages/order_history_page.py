from locators.order_history_locators import OrderHistoryPageLocators
from pages.base_page import BasePage
import allure

class OrderHistoryPage(BasePage):

    @allure.step('Получаем id первого заказа')
    def get_first_order_id(self):
        return self.get_text_from_element(OrderHistoryPageLocators.ORDER_ID)