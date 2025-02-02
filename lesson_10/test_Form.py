import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.MainPageForm import MainPageForm
import allure


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@allure.feature("Form Validation")
@allure.title("Test form input validation")
@allure.description("Testing if the form fields behave according to validation rules")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_validation(driver):
    with allure.step("Open main page and set cookie policy"):
        autoform = MainPageForm(driver)
        autoform.set_cookie_policy()

    with allure.step("Wait for elements by name"):
        autoform.waitbyname()

    with allure.step("Fill the form elements"):
        autoform.fill_form_element()

    with allure.step("Wait for elements by ID"):
        autoform.waitbyid()

    with allure.step("Check for validation error"):
        result = autoform.assert_red()
        assert "danger" in result.get_attribute("class"), "Zip Красное"

    fields = autoform.green_fields
    for f_id in fields:
        with allure.step(f"Check if field {f_id} is highlighted green"):
            assert "success" in autoform.assert_green(f_id).get_attribute(
                "class"
            ), f"Поле {f_id} должно быть подсвечено зеленым"