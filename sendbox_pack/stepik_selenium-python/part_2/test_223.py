from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

"""
Решение задачи + чекбокс и радиобаттон 
скролл ботома, закрывающего контент

1. Открыть страницу https://SunInJuly.github.io/execute_script.html.
2. Считать значение для переменной x.
3. Посчитать математическую функцию от x.
4. Проскроллить страницу вниз.
5. Ввести ответ в текстовое поле.
6. Выбрать checkbox "I'm the robot".
7. Переключить radiobutton "Robots rule!".
8. Нажать на кнопку "Submit".
"""
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    browser.execute_script("window.scrollBy(0, 300);")

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(15)
    browser.quit()
