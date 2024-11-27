from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка Войти в аккаунт на главной странице
    LOGIN_INTO_ACCOUNT_BUTTON = By.XPATH, "//button[text() = 'Войти в аккаунт']"
    # Кнопка Личный кабинет на главной странице
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[text() = 'Личный Кабинет']"
    # Кнопка Оформить заказ на главной странице
    MAKE_ORDER_BUTTON = By.XPATH, "//button[text() = 'Оформить заказ']"
    # Кнопка Конструктор в шапке страницы
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text() = 'Конструктор']"
    # Заголовок Соберите бургер
    MAKE_BURGER_HEADER = By.XPATH, "//h1[text() = 'Соберите бургер']"
    # Кнопка Лента заказов в шапке страницы
    ORDER_LIST_BUTTON = By.XPATH, "//p[text() = 'Лента Заказов']"
    # Флюоресцентная булка
    FLUORESCENT_BUN = By.XPATH, "//img[@alt = 'Флюоресцентная булка R2-D3']/parent::a"
    # Поле вверх для перетягивания булки
    FIELD_FOR_BUN_UP = By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]"
    # Счетчик булок
    BUN_COUNTER = By.XPATH, "//img[@alt = 'Флюоресцентная булка R2-D3']/parent::a/div[contains(@class, 'counter')]/p"
    # Текст Ваш заказ начали готовить во всплывающем окне при оформлении заказа
    ORDER_TEXT = By.XPATH, "//p[text() = 'Ваш заказ начали готовить']"
    # Идентификатор созданного заказа
    ORDER_ID = By.XPATH, "//h2[contains(@class, 'text_type_digits') and text() != '9999']"
    # Кнопка закрытия всплывающего окна заказа
    CLOSE_ORDER_WINDOW_BUTTON = By.XPATH, "//button[contains(@class, 'close')]"
