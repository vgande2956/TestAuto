import time
import pytest
from base.BasePage import BasePage
from utilities.ReadConfigFile import readConfig


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    user_name_credentials = "//div[@id='login_credentials']"
    password_credentials = "//div[@class='login_password']"
    username_text_box = "//input[@name='user-name']"
    password_text_box = "//input[@name='password']"
    login_button = "//input[@name='login-button']"

    def get_user_name(self):
        user_details = self.getText(self.user_name_credentials, "XPATH", "text")
        print(user_details)

    def get_password(self):
        password_details = self.getText(self.password_credentials, "XPATH", "text")
        print(password_details)

    # def login_page(self):
    #     self.type(self._user_TB, "XPATH", readConfig("Input", "user_name"))
    #     time.sleep(2)
    #     self.type(self._password_TB, "XPATH", readConfig("Input", "password"))
    #     time.sleep(2)
    #     self.click(self._sing_in_BTN, "XPATH")
    #
    # def urgentem_dashboard(self):
    #     self.urgentem_login()
    #     time.sleep(4)
    #     self.click(self._emissions_IC, "XPATH")
    #     self.click(self._footprint_Metric_filter, "XPATH")
    #     self.click(self._total_Carbon_Emissions_option, "XPATH")
    #     self.click(self._flm_IC, "XPATH")
    #     data = self.getText(self._footprint_Metric_text, "XPATH", "innerHTML")
    #     assert data == "Weighted Average Intensity (Revenue)", f"Got unexpected string value {data} instead of 'Weighted Average Intensity (Revenue)'."
