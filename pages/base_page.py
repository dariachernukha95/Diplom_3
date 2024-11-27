from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import data


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def move_to_element_and_click(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def fill_input_field(self, locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(text)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_for_element_becomes_invisible(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    # Для браузера Firefox не работает метод drag and drop из библиотеки ActionChains, поэтому для него добавлен работающий скрипт, который нам дал наставник
    def drag_and_drop_element(self, locator_from, locator_to):
        element_from = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator_from))
        element_to = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator_to))
        if data.driver_name == 'firefox':
            self.driver.execute_script("""
                                       var source = arguments[0];
                                       var target = arguments[1];
                                       var evt = document.createEvent("DragEvent");
                                       evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                                       source.dispatchEvent(evt);
                                       evt = document.createEvent("DragEvent");
                                       evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                                       target.dispatchEvent(evt);
                    evt = document.createEvent("DragEvent");
                                       evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                                       target.dispatchEvent(evt);
                                       evt = document.createEvent("DragEvent");
                                       evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                                       target.dispatchEvent(evt);
                                       evt = document.createEvent("DragEvent");
                                       evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                                       source.dispatchEvent(evt);
                                   """, element_from, element_to)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(element_from, element_to).perform()

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text