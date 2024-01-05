from selenium import webdriver  # By позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By  # Webdriver = набор команд для управления браузером
from selenium.webdriver.support.ui import Select  # Метод для работы со списками
import time  # Метод для установки задержек
import os  # Методы для работы с операционкой и использования файлов

try:  # блок try-finaly -- в них запизивать тесты


    # stay_open = options()
    # stay_open.add_experimental_option("detach", True)  # Оставляет браузер открытым
    # browser = webdriver.Chrome(options=stay_open)  # И когда инициализируешь переменную, в скобках добавляешь опцию

    browser = webdriver.Chrome()  # Инициализируем драйвер браузера == новое открытое окно браузера
    browser.get("https://suninjuly.github.io/text_input_task.html")  # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке

    textarea = browser.find_element(By.CSS_SELECTOR, ".textarea")  # Метод find_element находит нужный элемент (поле) на странице
    textarea.send_keys("test-test")  # Напишем текст в найденное поле

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

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    print(current_dir)
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла ??

    # В переменной file_path будет полный путь к файлу 'D:\stepik_homework\file.txt'.
    # если path изменится - код без правок все равно заработает

    # send_file_button = browser.find_element(By.CSS_SELECTOR, "[type='file']").click() - найти кнопку добавления файла
    # send_file_button.send_keys(file_path) # отправить файл

print(os.path.abspath(__file__))  # возвращает путь к прям вот этому исполняемому файлу
print(os.path.abspath(os.path.dirname(__file__)))  # возвращает путь к каталогу, где данный исполняемый файл
# это будет работать только при запуске кода из файла, в интерпретаторе не сработает.

os.path.exists("/sendbox_pack/stepik_selenium-python/file.txt")  # говорит, существует ли такой путь (к файлу)
print(os.path.exists("/sendbox_pack/stepik_selenium-python/file.txt"))








finally:
    time.sleep(5)  # Команда time.sleep устанавливает паузу в 5 секунд
    browser.quit()  # После выполнения всех действий мы должны не забыть закрыть окно браузера
