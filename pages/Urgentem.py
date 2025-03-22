import time
import pytest
from base.BasePage import BasePage
from utilities.ReadConfigFile import readConfig


class Urgentem(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _user_TB = "//input[@type = 'text']"
    _password_TB = "//input[@type = 'password']"
    _sing_in_BTN = "//div[@class= 'MuiBox-root jss22']/button"
    _emissions_IC = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[1]/*[1]"
    _footprint_Metric_filter = "//body/div[@id='root']/div[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]"
    _total_Carbon_Emissions_option = "//body/div[@id='root']/div[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]"
    _flm_IC = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/ul[1]/li[8]/a[1]/div[1]/*[1]"
    _footprint_Metric_text = "//*[@id='root']/div[1]/div/main/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]"

    # here i have read the data from a config file and running the test
    def urgentem_login(self):
        self.type(self._user_TB, "XPATH", readConfig("Input", "user_name"))
        time.sleep(2)
        self.type(self._password_TB, "XPATH", readConfig("Input", "password"))
        time.sleep(2)
        self.click(self._sing_in_BTN, "XPATH")

    def urgentem_dashboard(self):
        self.urgentem_login()
        time.sleep(4)
        self.click(self._emissions_IC, "XPATH")
        self.click(self._footprint_Metric_filter, "XPATH")
        self.click(self._total_Carbon_Emissions_option, "XPATH")
        self.click(self._flm_IC, "XPATH")
        data = self.getText(self._footprint_Metric_text, "XPATH", "innerHTML")
        assert data == "Weighted Average Intensity (Revenue)", f"Got unexpected string value {data} instead of 'Weighted Average Intensity (Revenue)'."
