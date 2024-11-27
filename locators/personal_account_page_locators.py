from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:
    # Текст на странице профиля "В этом разделе вы можете изменить свои персональные данные"
    DESCRIPTION_OF_PROFILE_PAGE = By.XPATH, "//p[text() = 'В этом разделе вы можете изменить свои персональные данные']"
    # Переход на страницу История заказов
    ORDER_HISTORY_LINK = By.XPATH, "//a[text() = 'История заказов']"
    # Кнопка Выход
    EXIT_BUTTON = By.XPATH, "//button[text() = 'Выход']"
