from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class Driver:

    def getDriverMethod(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        return driver