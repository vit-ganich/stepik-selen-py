from selenium import webdriver
import unittest
import time

class TestUnit(unittest.TestCase):
    '''Попробуйте оформить тесты из первого модуля в стиле unittest.

    Возьмите тесты из шага - https://stepik.org/lesson/138920/step/11?unit=196194
    Создайте новый файл
    Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
    Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
    Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
    Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
    Запустите получившиеся тесты из файла 
    Просмотрите отчёт о запуске и найдите последнюю строчку 
    Отправьте эту строчку в качестве ответа на это задание 
    Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. 
    Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. 
    Ловить исключения не надо (во всяком случае, здесь)!

    Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения. 

    Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке. 
    '''

    browser = None

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        if self.browser:
            self.browser.quit()

    def test_one(self):

        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)
        # Ваш код, который заполняет обязательные поля

        # Создаем шаблон локатора для трех обязательных элементов
        locator = "//label[text()='{0}']/following-sibling::input"

        # Применяем шаблон, подставляя разный текст
        self.browser.find_element_by_xpath(locator.format('First name*')).send_keys('Вот крот')
        self.browser.find_element_by_xpath(locator.format('Last name*')).send_keys('Вот хомяк')
        self.browser.find_element_by_xpath(locator.format('Email*')).send_keys('Хрум-хрум шмяк-шмяк')

        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, ч то смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEquals("Congratulations! You have successfully registered!", welcome_text)

if __name__ == '__main__':
    unittest.main()
    