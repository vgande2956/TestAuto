import unittest
import pytest
from pages.Urgentem import Urgentem
from pages.Urgentem_perameterized import Urgentem_perameterized
from utilities.ReadConfigFile import readConfig
from utilities.ExcelDataRead import getInputData
from parameterized import parameterized


# import utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethode")
class Urgentemtests(unittest.TestCase):
    valid_sheet = readConfig("Input", "sheet_name")
    valid_data = getInputData(valid_sheet)

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.bl = Urgentem(self.driver)
        self.up = Urgentem_perameterized(self.driver)

    # test with config file input data
    def test_Urgentem_Dashboard(self):
        self.bl.urgentem_dashboard()

    # test with excel input data perameterized to send the data as input
    @parameterized.expand(valid_data)
    @pytest.mark.excelInput
    def test__login_invalid_Credentials(self, User_name, password):
        self.up.urgentem_dashboard_parameterized(User_name, password)
