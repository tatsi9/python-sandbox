from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

"""
Работа с ереходом на новое окно

1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
2. Нажать на кнопку
3. Переключиться на новую вкладку
4. Пройти капчу для робота и получить число-ответ

"""

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    browser.find_element(By.CSS_SELECTOR, ".trollface[type = 'submit']").click()
    window_with_task = browser.window_handles[1]
    browser.switch_to.window(window_with_task)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, ".form-group [type='submit']").click()

finally:
    time.sleep(15)
    browser.quit()
