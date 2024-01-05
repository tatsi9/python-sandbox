from selenium import webdriver  # By позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By  # Webdriver = набор команд для управления браузером
from selenium.webdriver.support.ui import Select  # Метод для работы со списками
import time  # Метод для установки задержек
import os  # Методы для работы с операционкой и использования файлов

try:  # блок try-finaly -- в них запизивать тесты

    """ 
    # stay_open = options()
    # stay_open.add_experimental_option("detach", True)  # Оставляет браузер открытым
    # browser = webdriver.Chrome(options=stay_open)  # И когда инициализируешь переменную, в скобках добавляешь опцию
    """

    browser = webdriver.Chrome()  # Инициализируем драйвер браузера == новое открытое окно браузера
    browser.get("https://suninjuly.github.io/text_input_task.html")  # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке

    """ 
    либо
    link = "https://suninjuly.github.io/text_input_task.html"
    browser.get(link)
    """


    textarea = browser.find_element(By.CSS_SELECTOR, ".textarea")  # Метод find_element находит нужный элемент (поле) на странице
    textarea.send_keys("test-test")  # Напишем текст в найденное поле

    """ 
    ЕСЛИ find_element не смог найти элемент ==  NoSuchElementException прервёт выполнение вашего кода.
    find_elements - всегда возвращает валидный результат - минимум пустой список
    и программа перейдет к выполнению следующего шага в коде.
    """

    submit_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")  # Найдем кнопку, которая отправляет введенное решение
    submit_button.click()  # Нажать на кнопку

    x_element = browser.find_element(By.ID, "valuex")  # Найти элемент со значением
    x = x_element.text  # Вернуть найденный элемент как ТЕКСТ и записать в переменную (приводить к инту)

    option1 = browser.find_element(By.CSS_SELECTOR, "[value='python']")  # Найти радиобаттон или чекбокс
    option1.click()  # Ткнуть радиобаттон или чекбокс

    browser.find_element(By.TAG_NAME, "select").click()  # Выбрать выпадающий список и пункт списка - стандартные методы без импорта
    browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()  # Выбрать выпадающий список и пункт списка - стандартные методы без импорта
    browser.find_element(By.CSS_SELECTOR, "[value='1']").click()

    dropdown = Select(browser.find_element(By.TAG_NAME, "select")) # Выбрать выпадающий список и пункт списка (импортируемый метод)
    dropdown.select_by_value("1") # ищем элемент с текстом "Python"
    dropdown.select_by_visible_text("text")
    dropdown.select_by_visible_text("Python")  # ищет элемент по отображаемому тексту
    dropdown.select_by_index(1)  # ищет элемент по его индексу или порядковому номеру (с нуля)

    browser.execute_script("alert('Robots at work');")  # операции для запуска JS-cскриптов -- скроллы страниц
    browser.execute_script("document.title='Script executing';")
    browser.execute_script("document.title='Script executing';alert('Robots at work');")

    submit_button_disabled = people_radio.get_attribute("disabled")  # достает атрибут
    assert submit_button_disabled == "true", "The button is blocked"
    assert submit_button_disabled is None, "Robot radio is not selected by default"


finally:
    browser.quit()  # После выполнения всех действий мы должны не забыть закрыть окно браузера
    browser.close()  # Закрывает текущее окно браузера. Если есть всплывающие окно, то закроется только текущее.
