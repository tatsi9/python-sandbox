import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
Нахождение ссылки по имени и регистрационная форма
 
0. На странице  нужно найти зашифрованную ссылку и кликнуть по ней:
1. Добавьте в самый верх своего кода import math
2. Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
3. Добавьте команду, которая найдет ссылку с текстом. 
4. Текст ссылки, который нужно найти, зашифрован формулой: str(math.ceil(math.pow(math.pi, math.e)*10000))
5. Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
6. Заполните скриптом форму так же как вы делали в предыдущем шаге урока
7. После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание
"""


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")

    link_name = str(math.ceil(math.pow(math.pi, math.e)*10000))
    # хотим найти ссылку с текстом "Degree symbol in Math" и перейти по ней.


    link = browser.find_element(By.LINK_TEXT, link_name)
    link.click()

    # А если хотим найти элемент со ссылкой по подстроке, то нужно написать следующий код:
    # link = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Sandra")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Bulochka")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("megacity")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Veishnoria")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
