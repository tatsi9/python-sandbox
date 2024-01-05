from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

"""
Работа с алертом

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
"""

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    browser.find_element(By.CSS_SELECTOR, ".container [type='submit']").click()
    browser.switch_to.alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, ".form-group [type='submit']").click()

finally:
    time.sleep(15)
    browser.quit()
