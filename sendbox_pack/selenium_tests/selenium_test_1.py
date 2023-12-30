from selenium import webdriver

# Создание экземпляра драйвера (WebDriver)
driver = webdriver.Chrome()

# Взаимодействие с браузером, например, открытие веб-страницы
driver.get("https://docs.pytest.org/en/7.1.x/getting-started.html")

# Закрытие браузера
driver.quit()

# локация хромдрайвера:
# /usr/local/lib/node_modules/appium-uiautomator2-driver/node_modules/appium-chromedriver/chromedriver
