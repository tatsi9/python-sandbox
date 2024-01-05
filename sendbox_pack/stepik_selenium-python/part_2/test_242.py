from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
""" 
Нет ожиданий - падаем с неподгруженной кнопкой 
- Кнопка может быть неактивной (нельзя кликнуть)
- Кнопка может содержать меняющийся текст
- Кнопка может быть перекрыта каким-то другим элементом или быть невидимой
"""

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text
