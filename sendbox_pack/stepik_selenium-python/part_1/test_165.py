from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
Заполнение оч длинной формы

1. Дана страница с очень большой формой 
2. Используйте приведенный ниже шаблон
    в цикле for мы можем последовательно взять каждый элемент 
    из найденного списка текстовых полей и отправить произвольный текст в каждое поле. 
    Если скрипт не успевает заполнить форму, выберите текст покороче. 
3. Нажмите кнопку, чтобы отправить
"""


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")  # (By.TAG_NAME, "br")
    for element in elements:
        element.send_keys("поньк")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

