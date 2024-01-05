from selenium import webdriver
from selenium.webdriver.common.by import By

""" 
Нет ожиданий - падаем с неподгруженной кнопкой 

1. Открыть страницу http://suninjuly.github.io/wait1.html
2. Нажать на кнопку "Verify"
3. Проверить, что появилась надпись "Verification was successful!"
"""

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
# time.sleep(2)
browser.implicitly_wait(5)

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text # находим новый элемент с текстом и проверяем соответствие текста на странице ожидаемому тексту.

