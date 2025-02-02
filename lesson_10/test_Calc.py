import pytest
from selenium import webdriver
from Pages.MainPageСalc import MainPageCalc
from selenium.webdriver.chrome.options import Options
import allure


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@allure.feature("Calculator")
@allure.title("Test calculator functionality")
@allure.description(
    "Test the calculator's ability to perform a calculation with a specified delay"
)
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(driver):
    with allure.step("Set cookie policy"):
        calc = MainPageCalc(driver)
        calc.set_cookie_policy()

    with allure.step("Wait for elements to load"):
        calc.wait_for_elements()

    with allure.step("Enter time delay"):
        calc.enter_time_delay(45)

    with allure.step("Enter expression"):
        calc.enter_expression()

    with allure.step("Get result"):
        result = calc.get_result()

    with allure.step("Check the result"):
        assert result == "15", f"Ошибка: Ожидалось '15', но получено '{result}'"