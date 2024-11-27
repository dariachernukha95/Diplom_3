from selenium.webdriver.common.by import By

class LoginPageLocators:
    # Кнопка Восстановить пароль
    RECOVER_PASSWORD_BUTTON = By.XPATH, "//a[@href = '/forgot-password']"
    # Поле ввода Email
    INPUT_FIELD_EMAIL = By.XPATH, "//label[text() = 'Email']/parent::div/input"
    # Поле ввода Пароль
    INPUT_FIELD_PASSWORD = By.XPATH, "//label[text() = 'Пароль']/parent::div/input"
    # Кнопка Войти
    LOGIN_BUTTON = By.XPATH, "//button[text() = 'Войти']"
    # Заголовок формы Вход
    LOGIN_HEADER = By.XPATH, "//h2[text() = 'Вход']"