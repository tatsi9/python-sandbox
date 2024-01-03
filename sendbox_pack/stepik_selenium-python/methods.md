import time
from selenium import webdriver
# Импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
# Webdriver это и есть набор команд для управления браузером
from selenium.webdriver.support.ui import Select
# Импортируем метод для работы со списками


driver = webdriver.Chrome()
# Инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера

driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(5)
# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# Команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере

textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
textarea.send_keys("test-test")
# Метод find_element находит нужный элемент (поле) на странице
# Напишем текст в найденное поле

submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
submit_button.click()

# Найдем кнопку, которая отправляет введенное решение
# Нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе

driver.quit()
# После выполнения всех действий мы должны не забыть закрыть окно браузера

x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
x = x_element.text
## Вернуть найденный элемент как текст

option1 = browser.find_element(By.CSS_SELECTOR, "[value='python']")
option1.click()
## Выбрать радиобаттон или чекбокс

browser.find_element(By.TAG_NAME, "select").click()
browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
browser.find_element(By.CSS_SELECTOR, "[value='1']").click()
## Выбрать выпадающий список и поинт - стандартные методы без импорта 

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1") # ищем элемент с текстом "Python"
select.select_by_visible_text("text")
select.select_by_visible_text("Python") -- ищет элемент по видимому тексту
select.select_by_index(1) -- ищет элемент по его индексу или порядковому номеру (с нуля)
## Выбрать выпадающий список и поинт - етоды с импортом

o = Options()
o.add_experimental_option("detach", True)
## И когда инициализируешь переменную, в скобках добавляешь опцию
browser = webdriver.Chrome(options=o)
## Оставляет браузер открытым


browser.execute_script("alert('Robots at work');")
browser.execute_script("document.title='Script executing';")
browser.execute_script("document.title='Script executing';alert('Robots at work');")
