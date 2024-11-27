from selenium.webdriver.common.by import By

class OrderListPageLocators:
    # Заголовок Лента заказов
    ORDER_LIST_HEADER = By.XPATH, "//h1[text() = 'Лента заказов']"
    # Карточка заказа
    ORDER_CARD = By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]"
    # Всплывающее окно с деталями заказа
    ORDER_WINDOW = By.XPATH, "//div[contains(@class, 'Modal_orderBox')]"
    # Список заказов в работе
    ORDER_LIST_IN_WORK = By.XPATH, "//ul[contains(@class, 'orderListReady')]/li[text() != 'Все текущие заказы готовы!']"
    # Идентификатор заказа последнего заказа
    LAST_ORDER_ID = By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]//p[contains(@class, 'text_type_digits')]"
    # Счетчик выполненных за все время заказов
    ALL_ORDERS_COUNTER = By.XPATH, "//p[text() = 'Выполнено за сегодня:']/parent::div/p[contains(@class, 'text_type_digits')]"
    # Счетчик выполненных за cегодня заказов
    TODAY_ORDERS_COUNTER = By.XPATH, "//p[text() = 'Выполнено за все время:']/parent::div/p[contains(@class, 'text_type_digits')]"