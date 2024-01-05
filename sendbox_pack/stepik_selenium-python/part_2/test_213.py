from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

"""
Решение задачи + чекбокс и радиобаттон 
со спрятанным x в атрибутах

1. Открыть страницу http://suninjuly.github.io/get_attribute.html.
2. Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
4. Посчитать математическую функцию от x (сама функция остаётся неизменной).
5. Ввести ответ в текстовое поле.
6. Отметить checkbox "I'm the robot".
7. Выбрать radiobutton "Robots rule!".
8. Нажать на кнопку "Submit".
"""
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/get_attribute.html")

    treasure_icon = browser.find_element(By.ID, "treasure")
    treasure_value = treasure_icon.get_attribute("valuex")
    x = treasure_value
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    time.sleep(2)
    browser.find_element(By.ID, "robotCheckbox").click()
    time.sleep(2)
    browser.find_element(By.ID, "robotsRule").click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "[type = submit]").click()

finally:
    time.sleep(5)
    browser.quit()
