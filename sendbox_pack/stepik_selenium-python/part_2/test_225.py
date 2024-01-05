from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

"""
1. Открыть страницу http://suninjuly.github.io/file_input.html
2. Заполнить текстовые поля: имя, фамилия, email
3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
4. Нажать кнопку "Submit"

"""

try:
    browser = webdriver.Chrome()  # Инициализируем драйвер браузера == новое открытое окно браузера
    browser.get("http://suninjuly.github.io/file_input.html")  # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке

    input_fname = browser.find_element(By.NAME, "firstname")
    input_fname.send_keys("Поньк")

    input_lname = browser.find_element(By.NAME, "lastname")
    input_lname.send_keys("Поньк")

    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("Поньк")

    file_button = browser.find_element(By.ID, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file_button.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()
