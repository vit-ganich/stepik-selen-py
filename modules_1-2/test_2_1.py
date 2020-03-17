from selenium import webdriver
import time
import math

'''Ваша программа должна выполнить следующие шаги:

Открыть страницу http://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit.
Для этой задачи вам понадобится использовать атрибут .text для найденного элемента. Обратите внимание, что скобки здесь не нужны:

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
'''


try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_css_selector("#input_value").text
    answer = str(math.log(abs(12*math.sin(int(x)))))

    text_field = browser.find_element_by_css_selector("#answer")
    text_field.send_keys(answer)

    robot_checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    robot_checkbox.click()

    robot_radio = browser.find_element_by_css_selector("#robotsRule")
    robot_radio.click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn-default")
    button.click()

    # Проверяем, ч то смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    alert=browser.switch_to_alert() 
    print(alert.text) 
    # закрываем браузер после всех манипуляций
    browser.quit()