from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
Пример использования get_attribute
"""

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    # assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None, "Robot radio is not selected by default"

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type = submit]")
    submit_button_disabled = people_radio.get_attribute("disabled")
    assert submit_button_disabled == "true", "The button is blocked"

finally:
    time.sleep(5)
    browser.quit()




