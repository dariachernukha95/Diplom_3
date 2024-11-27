


class TestLogIn:
    def test_change_password(self, driver):
        driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.CHANGE_PASSWORD_BUTTON).click()
        driver.find_element(*Locators.LOGIN_BUTTON_ON_REGISTRATION_PAGE).click()
        driver.find_element(*Locators.INPUT_FIELD_EMAIL).send_keys("dariachernukha14465@yandex.ru")
        driver.find_element(*Locators.INPUT_FIELD_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(Locators.LOGIN_INTO_ACCOUNT_BUTTON, "Оформить заказ"))
        make_order_button_text = driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON).text
        assert make_order_button_text == 'Оформить заказ'