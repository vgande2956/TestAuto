import unittest
import pytest
from pages.Login_page import LoginPage
from utilities.ReadConfigFile import readConfig
from utilities.ExcelDataRead import getInputData
from parameterized import parameterized


# import utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass")
class LoginTests(unittest.TestCase):
    # valid_sheet = readConfig("Input", "sheet_name")
    # valid_data = getInputData(valid_sheet)

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = LoginPage(self.driver)

    # test with config file input data
    def test_login_page(self):
        self.bl.urgentem_dashboard()
