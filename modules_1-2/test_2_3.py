from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from test_base import TestBase
import time

class TestOne(TestBase):
    '''Задание: ждем нужный текст на странице
    Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. 
    Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

    В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

    Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    Нажать на кнопку "Book"
    Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    Чтобы определить момент, когда цена аренды уменьшится до $100, 
    используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

    Если все сделано правильно и быстро, то вы увидите окно с числом. 
    Отправьте его в качестве ответа на это задание.
    '''

    def test_three(self, browser):

        link = "http://suninjuly.github.io/explicit_wait2.html"
        browser.get(link)

        text = self.waitForLowPrice(browser, (By.ID, 'price'), '$100', timeout=15)

        button = self.waitForClick(browser, (By.ID, 'book'))
        button.click()
        script = "arguments[0].click()"

        number = self.waitForClick(browser, (By.ID, 'input_value'))
        browser.execute_script(script, number)

        x = number.text

        x = self.calc(x)

        text_box = self.waitForClick(browser, (By.ID, 'answer'))
        text_box.send_keys(x)

        button = self.waitForClick(browser, (By.ID, 'solve'))
        button.click()
        time.sleep(10)
        # alert=browser.switch_to_alert() 
        # print(alert.text) 

    def waitForClick(self, driver, locator, timeout=5):
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator))

    def waitForLowPrice(self, driver, locator, price, timeout=5):
        return WebDriverWait(driver, timeout).until(
            EC.text_to_be_present_in_element(locator, price)
        )
