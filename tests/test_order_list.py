import allure
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.personal_account_page import PersonalAccountPage
from pages.order_history_page import OrderHistoryPage


class TestOrderList:
    @allure.title('Проверка открытия всплывающего окна с деталями заказа')
    def test_open_order_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_list_button()
        order_list_page = OrderListPage(driver)
        order_list_page.click_first_order_card()
        assert order_list_page.find_order_window()

    @allure.title('Проверка отображения заказов пользователя из раздела «История заказов» на странице «Лента заказов»')
    def test_users_order_from_order_history_in_order_list(self, driver, log_in):
        main_page = MainPage(driver)
        main_page.drag_and_drop_bun()
        main_page.click_make_order_button()
        main_page.find_order_id()
        main_page.click_close_order_window_button()
        main_page.click_personal_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_order_history_link()
        order_history_page = OrderHistoryPage(driver)
        order_id_in_order_history = order_history_page.get_first_order_id()
        main_page.click_order_list_button()
        order_list_page = OrderListPage(driver)
        last_order_id_in_order_list = order_list_page.get_last_order_in_order_list()
        assert order_id_in_order_history == last_order_id_in_order_list

    @allure.title('Проверка увеличения значения счетчика выполненных за все время заказов после оформления заказа')
    def test_all_orders_counter_raise_after_making_order(self, driver, log_in):
        main_page = MainPage(driver)
        main_page.click_order_list_button()
        order_list_page = OrderListPage(driver)
        all_orders_value_before_making_order = int(order_list_page.get_all_orders_value())
        main_page.click_constructor_button()
        main_page.drag_and_drop_bun()
        main_page.click_make_order_button()
        main_page.find_order_id()
        main_page.click_close_order_window_button()
        main_page.click_order_list_button()
        all_orders_value_after_making_order = int(order_list_page.get_all_orders_value())
        assert all_orders_value_after_making_order > all_orders_value_before_making_order

    @allure.title('Проверка увеличения значения счетчика выполненных за сегодня заказов после оформления заказа')
    def test_today_orders_counter_raise_after_making_order(self, driver, log_in):
        main_page = MainPage(driver)
        main_page.click_order_list_button()
        order_list_page = OrderListPage(driver)
        today_orders_value_before_making_order = int(order_list_page.get_today_orders_value())
        main_page.click_constructor_button()
        main_page.drag_and_drop_bun()
        main_page.click_make_order_button()
        main_page.find_order_id()
        main_page.click_close_order_window_button()
        main_page.click_order_list_button()
        today_orders_value_after_making_order = int(order_list_page.get_today_orders_value())
        assert today_orders_value_after_making_order > today_orders_value_before_making_order

    @allure.title('Проверка отображения созданного заказа в разделе В работе')
    def test_users_order_in_order_list(self, driver,log_in):
        main_page = MainPage(driver)
        main_page.drag_and_drop_bun()
        main_page.click_make_order_button()
        order_id = main_page.get_order_id()
        main_page.click_close_order_window_button()
        main_page.click_order_list_button()
        order_list_page = OrderListPage(driver)
        order_list_in_work = order_list_page.get_order_list_in_work()
        assert order_id in order_list_in_work
