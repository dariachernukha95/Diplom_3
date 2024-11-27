import allure
from data import base_url, order_list_url, ingredient_url
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.personal_account_page import PersonalAccountPage
from pages.ingredient_page import IngredientPage


class TestMainFunctional:
    @allure.title('Проверка перехода в раздел Конструктор')
    def test_go_to_constructor_page(self, driver, log_in):
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.find_description_of_profile_page()
        main_page.click_constructor_button()
        main_page.find_make_burger_header()
        assert driver.current_url == base_url

    @allure.title('Проверка перехода в раздел Лента заказов')
    def test_go_to_order_list_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_list_button()
        order_list_page = OrderListPage(driver)
        order_list_page.find_order_list_header()
        assert driver.current_url == order_list_url

    @allure.title('Проверка появления всплывающего окна с деталями об ингредиенте при нажатии на него')
    def test_check_ingredient_window_by_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun()
        ingredient_page = IngredientPage(driver)
        ingredient_page.find_ingredient_details_header()
        assert ingredient_url in driver.current_url

    @allure.title('Проверка закрытия всплывающего окна с деталями об ингредиенте')
    def test_close_ingredient_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun()
        ingredient_page = IngredientPage(driver)
        ingredient_page.find_ingredient_details_header()
        ingredient_page.click_close_button()
        assert ingredient_page.wait_for_ingredient_window_closing()

    @allure.title('Проверка добавления ингредиента к заказу')
    def test_add_ingredient_to_order(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_bun()
        counter_value = main_page.get_bun_counter_value()
        assert counter_value == '2'

    @allure.title('Проверка оформления заказа залогиненным пользователем')
    def test_make_order_by_authorized_user(self, driver, log_in):
        main_page = MainPage(driver)
        main_page.drag_and_drop_bun()
        main_page.click_make_order_button()
        assert main_page.find_order_confirmation()
