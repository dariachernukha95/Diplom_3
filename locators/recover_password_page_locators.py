from selenium.webdriver.common.by import By

class RecoverPasswordPageLocators:
    # Заголовок формы Восстановление пароля
    RECOVER_PASSWORD_HEADER = By.XPATH, '//h2[text() = "Восстановление пароля"]'
    # Поле ввода Email
    EMAIL_INPUT_FIELD = By.XPATH, '//input[@class = "text input__textfield text_type_main-default"]'
    # Кнопка Восстановить
    RECOVER_BUTTON = By.XPATH, '//button[text() = "Восстановить"]'
    # Поле ввода Пароль со скрытым паролем
    PASSWORD_INPUT_FIELD_HIDDEN = By.XPATH, '//input[@type = "password"]'
    # Поле ввода Пароль с открытым паролем
    PASSWORD_INPUT_FIELD_VISIBLE = By.XPATH, '//input[@type = "text"]'
    # Кнопка показать/скрыть пароль
    SHOW_PASSWORD_BUTTON = By.XPATH, '//div[@class = "input__icon input__icon-action"]'
    # Активный статус поле ввода Пароль при нажатии на кнопку Показать пароль
    ACTIVE_STATUS_OF_INPUT_FIELD = By.XPATH, '//div[contains(@class, "input_status_active")]'


