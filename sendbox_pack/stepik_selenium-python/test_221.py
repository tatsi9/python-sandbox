"""
Работа со списками
1. Открыть страницу https://suninjuly.github.io/selects1.html
2. Посчитать сумму заданных чисел
3. Выбрать в выпадающем списке значение равное рассчитанной сумме
4. Нажать кнопку "Submit"
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")
    num_1 = int(num1_element.text)
    num_2 = int(num2_element.text)
    answer = str(num_1 + num_2)

    # browser.find_element(By.ID, "dropdown").click()  # работает
    # browser.find_element(By.CSS_SELECTOR, f"#dropdown > option[value='{answer}']").click()  # работает
    # time.sleep(2)

    dropdown_answers = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    dropdown_answers.select_by_visible_text(str(answer))
    time.sleep(2)

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type = submit]")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
