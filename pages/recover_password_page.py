from selenium.webdriver.common.by import By

class LoginPageLocators:
    # Кнопка Восстановить пароль
    CHANGE_PASSWORD_BUTTON = (By.XPATH, "//a[@class = 'Auth_link__1fOlj']")