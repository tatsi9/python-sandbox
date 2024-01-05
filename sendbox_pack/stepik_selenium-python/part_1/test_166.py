from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
Заполнение оч длинной формы - обращение по XPath

1. В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
2. Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit. 
    XPath можете формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
3. Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
4. Запустите ваш код.
"""

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
# value1, value2 -- значения нужно заключать в кавычки, т.к. они должны передаваться в виде строки.
