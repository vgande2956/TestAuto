import time
import pytest
from base.DriverClass import Driver


@pytest.fixture(scope="class")
def beforeClass(request):
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
        driver.implicitly_wait(10)
    yield driver
    time.sleep(5)
    driver.quit()


@pytest.fixture()
def beforeMethode():
    print("Before Methode")
    yield
    print("After Methode")
