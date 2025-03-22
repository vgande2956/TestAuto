import time
import allure
from allure_commons.types import AttachmentType
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.CustomLogger import customLogger

class BasePage:
    log = customLogger()

    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 25, poll_frequency=1, ignored_exceptions=(
            ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException))

    def click(self, locatorValue, locatorType):
        time.sleep(10)
        if str(locatorType) == "XPATH":
            self.driver.find_element(By.XPATH, locatorValue).click()
            self.log.info("Clicked on the element ::  " + locatorValue)
        elif str(locatorType) == "NAME":
            self.driver.find_element(By.NAME, locatorValue).click()
            self.log.info("Clicked on the element ::  " + locatorValue)
        elif str(locatorType) == "ID":
            self.driver.find_element(By.ID, locatorValue).click()
            self.log.info("Clicked on the element ::  " + locatorValue)

    def type(self, locatorValue, locatorType, value):
        if str(locatorType) == "XPATH":
            self.driver.find_element(By.XPATH, locatorValue).send_keys(value)
            self.log.info("Enter the text value as : " + str(value) + "to the element : " + locatorValue)
        elif str(locatorType) == "NAME":
            self.driver.find_element(By.NAME,
                                     locatorValue).send_keys(value)
            self.log.info("Enter the text value as : " + str(value) + "to the element : " + locatorValue)
        elif str(locatorType) == "ID":
            self.driver.find_element(By.ID, locatorValue).send_keys(value)
            self.log.info("Enter the text value as : " + str(value) + "to the element : " + locatorValue)

    def getText(self, locatorValue, locatorType, type):
        element = None
        # time.sleep(5)
        if type == "innerHTML":
            if str(locatorType) == "XPATH":
                element = self.driver.find_element(By.XPATH, locatorValue).get_attribute('innerHTML')
                self.log.info("element value is :: " + element)
                return element
            elif str(locatorType) == "NAME":
                element = self.driver.find_element(By.NAME, locatorValue).get_attribute(
                    'innerHTML')
                self.log.info("element value is :: " + element)
                return element
            elif str(locatorType) == "ID":
                element = self.driver.find_element(By.ID, locatorValue).get_attribute('innerHTML')
                self.log.info("element value is :: " + element)
                return element
            return element
        elif type == "text":
            if str(locatorType) == "XPATH":
                element = self.driver.find_element(By.XPATH, locatorValue).get_attribute('text')
                self.log.info("element value is :: " + element)
                return element
            elif str(locatorType) == "NAME":
                element = self.driver.find_element(By.NAME, locatorValue).get_attribute('text')
                self.log.info("element value is :: " + element)
                return element
            elif str(locatorType) == "ID":
                element = self.driver.find_element(By.ID, locatorValue).get_attribute('text')
                self.log.info("element value is :: " + element)
                return element
            return element
        return element

    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + time.strftime("%d_%m_%y_%H_%M_%S") + ".png"
        screenShotDirectory = "../screenshots/"
        screenShotsPath = screenShotDirectory + fileName
        try:
            self.driver.save_screenshot(screenShotsPath)
            self.log.info("screen shot save to path " + screenShotsPath)
        except:
            self.log.info("Unable to save screenshot to path")

    def takeScreenShot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

