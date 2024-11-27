from selenium.webdriver.common.by import By

class OrderListPageLocators:
    # Заголовок Лента заказов
    ORDER_LIST_HEADER = By.XPATH, "//h1[text() = '']"