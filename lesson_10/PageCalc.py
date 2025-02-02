import pytest
from selenium import webdriver
from Pages.MainPageCalc import MainPageCalc
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_calculator(driver):
    calc = MainPageCalculator(driver)
    calc.set_cookie_policy()
    calc.wait_for_elements()
    calc.enter_time_delay(45)
    calc.enter_expression()
    result = calc.get_result()
    assert result == "15", "Ошибка?!"