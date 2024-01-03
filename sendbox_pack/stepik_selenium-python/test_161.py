from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/simple_form_find_task.html")
element = browser.find_element(By.ID, "timeLeft")
button = browser.find_element(By.ID, "submit_button")
button.click()
browser.quit()


# browser.close()
# закрывает текущее окно браузера. Если есть всплывающие окно, то закроется только текущее.
# browser.quit()
# закрывает все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии.

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
