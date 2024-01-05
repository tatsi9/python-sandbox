from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # Метод для установки задержек
from selenium.webdriver.support.ui import WebDriverWait  # Методы для эксплицитных задержек
from selenium.webdriver.support import expected_conditions as EC

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait2.html")

    time.sleep(5)  # Команда time.sleep устанавливает абсолютную задержку в 5 секунд

    """ 
    Исключения: 
    NoSuchElementException - элемент не был найден за отведенное время
    StaleElementReferenceException -  элемент был найден в момент поиска, но при обращении DOM изменился (например скрыт скриптом)
    ElementNotVisibleException - элемент был найден в момент поиска, но он невидим (например нулевые размеры)
    """

    """
    Implisity 
    Ждет до n-секунд и проверяет есть ли элемент каждые 0.5с 
    получая элемент - делает операцию и идет дальше
    не нужно ниче импортировать
    """

    browser.implicitly_wait(5)  # ждем до 5с и проверяя есть ли элемент каждые 0.5с и идем дальше

    """
    Explicity
    element_to_be_clickable вернет элемент, с заданным состоянием (напр. кликабельным) или False
    Функция until (until_not) - передается правило ожидания, элемент и значение для поиска элемента. 
    Другие правила для ожиданий:
    title_is
    title_contains
    presence_of_element_located
    visibility_of_element_located
    visibility_of
    presence_of_all_elements_located
    text_to_be_present_in_element
    text_to_be_present_in_element_value
    frame_to_be_available_and_switch_to_it
    invisibility_of_element_located
    element_to_be_clickable
    staleness_of
    element_to_be_selected
    element_located_to_be_selected
    element_selection_state_to_be
    element_located_selection_state_to_be
    alert_is_present
    """

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )  # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

    button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )  # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной

finally:
    browser.quit()




