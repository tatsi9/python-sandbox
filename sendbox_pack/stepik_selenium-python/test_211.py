from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    time.sleep(2)

    checkbox_robot = browser.find_element(By.ID, "robotCheckbox")
    checkbox_robot.click()
    time.sleep(2)

    radio_robot = browser.find_element(By.ID, "robotsRule")
    radio_robot.click()
    time.sleep(2)

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type = submit]")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()




