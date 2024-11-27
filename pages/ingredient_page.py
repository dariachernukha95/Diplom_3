from locators.ingredient_page_locators import IngredientPageLocators
from pages.base_page import BasePage
import allure

class IngredientPage(BasePage):
    @allure.step('Находим заголовок Детали ингредиента в окне ингредиента')
    def find_ingredient_details_header(self):
        self.find_element_with_wait(IngredientPageLocators.INGREDIENT_DETAILS_HEADER)

    @allure.step('Нажимаем на кнопку в виде крестика')
    def click_close_button(self):
        self.move_to_element_and_click(IngredientPageLocators.CLOSE_BUTTON)

    @allure.step('Ожидаем пока всплывающее окно игредиента исчезнет')
    def wait_for_ingredient_window_closing(self):
        return self.wait_for_element_becomes_invisible(IngredientPageLocators.INGREDIENT_DETAILS_HEADER)