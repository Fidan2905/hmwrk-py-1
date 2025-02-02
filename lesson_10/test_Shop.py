import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.InventoryPageShop import InventoryPageShop
from Pages.CartPageShop import CartPageShop
from Pages.CheckOutPageShop import CheckOutPageShop
from Pages.OverviewPageShop import OverviewPageShop
from Pages.MainPageShop import MainPageShop
import allure


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@allure.feature("Internet Shop")
@allure.title("Test checkout process")
@allure.description("Testing the full checkout process in the internet shop")
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout_process(driver):
    with allure.step("Open main page and set cookie policy"):
        shop = MainPageShop(driver)
        shop.set_cookie_policy()
        shop.wait()

    with allure.step("Login to the shop"):
        shop.enterloginpass()

    with allure.step("Navigate to inventory page and set cookie policy"):
        shop = InventoryPageShop(driver)
        shop.set_cookie_policy()
        shop.wait()

    with allure.step("Add item to basket"):
        shop.additemintobasket()

    with allure.step("Navigate to cart page and set cookie policy"):
        shop = CartPageShop(driver)
        shop.set_cookie_policy()
        shop.wait()

    with allure.step("Press checkout button"):
        shop.checkoutpress()

    with allure.step("Navigate to checkout page and set cookie policy"):
        shop = CheckOutPageShop(driver)
        shop.set_cookie_policy()
        shop.wait()

    with allure.step("Press continue button"):
        shop.Continuepress()

    with allure.step("Navigate to overview page and set cookie policy"):
        shop = OverviewPageShop(driver)
        shop.set_cookie_policy()
        shop.wait()

    with allure.step("Verify total amount"):
        txt = shop.Equal()
        assert (
            txt == "Total: $58.29"
        ), f"Error! Expected 'Total: $58.29', but got '{txt}'"