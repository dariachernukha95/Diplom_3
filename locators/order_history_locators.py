from selenium.webdriver.common.by import By

class OrderHistoryPageLocators:
    # Идентификатор заказа
    ORDER_ID = By.XPATH, "//ul[contains(@class, 'OrderHistory_list')]/li[1]//p[contains(@class, 'text_type_digits')]"
