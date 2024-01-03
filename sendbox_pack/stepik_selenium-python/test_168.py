from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # link = "https://suninjuly.github.io/registration1.html"
    # Старая ссылка. Перед использованием - закомментировать новую!

    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняются обязательные поля
    input_name = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.first_class > input")
    input_name.send_keys("Поньк")
    input_last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.second_class > input")
    input_last_name.send_keys("Поньк")
    input_email = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.third_class > input")
    input_email.send_keys("Поньк")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
