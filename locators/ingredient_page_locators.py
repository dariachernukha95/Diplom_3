from selenium.webdriver.common.by import By

class IngredientPageLocators:

    # Заголовок Детали ингредиента во всплывающем окне ингредиента
    INGREDIENT_DETAILS_HEADER = By.XPATH, "//h2[text() = 'Детали ингредиента']"
    # Кнопка закрытия всплывающего окна ингредиента
    CLOSE_BUTTON= By.XPATH, "//button[contains(@class, 'Modal_modal__close')]"
