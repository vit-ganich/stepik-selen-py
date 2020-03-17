from selenium import webdriver
import time


try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля

    # Создаем шаблон локатора для трех обязательных элементов
    locator = "//label[text()='{0}']/following-sibling::input"

    # Применяем шаблон, подставляя разный текст
    browser.find_element_by_xpath(locator.format('First name*')).send_keys('Вот крот')
    browser.find_element_by_xpath(locator.format('Last name*')).send_keys('Вот хомяк')
    browser.find_element_by_xpath(locator.format('Email*')).send_keys('Хрум-хрум шмяк-шмяк')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, ч то смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # alert=browser.switch_to_alert() 
    # print(alert.text) 
    # закрываем браузер после всех манипуляций
    browser.quit()