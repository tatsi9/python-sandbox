from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
Регистрационная форма - правильные селекторы

1. Тест успешно проходит на странице http://suninjuly.github.io/registration1.html
2. Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html
3. Используемые селекторы должны быть уникальны
"""

link1 = "https://suninjuly.github.io/registration1.html"
link2 = "https://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link1)

    input_name = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.first_class > input")
    input_name.send_keys("Поньк")
    input_last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.second_class > input")
    input_last_name.send_keys("Поньк")
    input_email = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.third_class > input")
    input_email.send_keys("Поньк")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
