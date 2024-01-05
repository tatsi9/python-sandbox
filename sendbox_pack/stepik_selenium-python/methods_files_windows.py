from selenium import webdriver  # By позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By  # Webdriver = набор команд для управления браузером
from selenium.webdriver.support.ui import Select  # Метод для работы со списками
import time  # Метод для установки задержек
import os  # Методы для работы с операционкой и использования файлов

try:
    # stay_open = options()
    # stay_open.add_experimental_option("detach", True)  # Оставляет браузер открытым
    # browser = webdriver.Chrome(options=stay_open)  # И когда инициализируешь переменную, в скобках добавляешь опцию

    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/text_input_task.html")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'part_2/file.txt')  # добавляем к этому пути имя файла ??

    send_file_button = browser.find_element(By.CSS_SELECTOR, "[type='file']").click()  # найти кнопку добавления файла
    send_file_button.send_keys(file_path)  # отправить файл


    alert = browser.switch_to.alert # переключиться на модальное окно
    alert_text = alert.text # получить текст с алерта
    alert.accept() # нажать ок, чтобы закрылось - если одна кнопка

    confirmation = browser.switch_to.alert
    confirmation.accept()  # нажать ок и закрыть (двухкнопочный алерт = confirmation)
    confirmation.dismiss()  # нажать нет и закрыть (двухкнопочный алерт = confirmation)

    prompt = browser.switch_to.alert
    prompt.send_keys("My answer")  # ввести строку в алерт с полем ввода (prompt)
    prompt.accept()  # нажать ок и закрыть алерт (prompt)
    prompt.dismiss()  # нажать нет и закрыть алерт (prompt)


    """
    WebDriver может работать только с одной вкладкой браузера
    после переключения на вкладку - действия дальше только на ней
    window_handles возвращает массив всех вкладок и имен
    """

    new_window = browser.window_handles[1]  # открыть вторую по счету вкладку
    first_window = browser.window_handles[0]  # запомнить имя текущей вкладки, чтобы потом вернуться
    browser.switch_to.window(new_window)  # переключиться на новую вкладку с указат елем





finally:
    time.sleep(5)  # Команда time.sleep устанавливает паузу в 5 секунд
    browser.quit()  # После выполнения всех действий мы должны не забыть закрыть окно браузера
