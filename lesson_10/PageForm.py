from Pages.MainPageForm import MainPageForm
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_Calc():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options)
    autoform = MainPageForm(driver)
    autoform.set_cookie_policy()
    autoform.waitbyname()
    autoform.fill_form_element()
    autoform.waitbyid()
    result = autoform.assert_red()
    assert "danger" in result.get_attribute("class"), "Zip Красное"
    fields = autoform.green_fields
    for f_id in fields:
        assert "success" in autoform.assert_green(f_id).get_attribute(
            "class"
        ), f"Поле {f_id} должен подсвечиваться зеленым"