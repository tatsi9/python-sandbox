from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
Пример использования execute_script
"""

browser = webdriver.Chrome()
browser.get("https://SunInJuly.github.io/execute_script.html")
time.sleep(4)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(4)

browser.execute_script("window.scrollBy(0, 100);")
time.sleep(4)

browser.quit()
