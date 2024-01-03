"""
1. Открыть страницу https://SunInJuly.github.io/execute_script.html.
2. Считать значение для переменной x.
3. Посчитать математическую функцию от x.
4. Проскроллить страницу вниз.
5. Ввести ответ в текстовое поле.
6. Выбрать checkbox "I'm the robot".
7. Переключить radiobutton "Robots rule!".
8. Нажать на кнопку "Submit".
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    browser.execute_script("window.scrollBy(0, 300);")
    checkbox_robot = browser.find_element(By.ID, "robotCheckbox")
    checkbox_robot.click()

    radio_robot = browser.find_element(By.ID, "robotsRule")
    radio_robot.click()

    button = browser.find_element(By.TAG_NAME, "button")

    button.click()

finally:
    time.sleep(15)
    browser.quit()
