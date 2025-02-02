import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.InventoryPageShop import InventoryPageShop
from Pages.CartPageShop import CartPageShop
from Pages.CheckOutPageShop import CheckoutPageShop
from Pages.CheckOutPageShop import OverviewPageShop
from Pages.MainPageShop import MainPageShop


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_Calc():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options)
    shop = MainPageShop(driver)
    shop.set_cookie_policy()
    shop.wait()
    shop.enterloginpass()
    shop = InventoryPageShop(driver)
    shop.set_cookie_policy()
    shop.wait()
    shop.additemintobasket()
    shop = CartPageShop(driver)
    shop.set_cookie_policy()
    shop.wait()
    shop.checkoutpress()
    shop = CheckoutPageShop(driver)
    shop.set_cookie_policy()
    shop.wait()
    shop.Continuepress()
    shop = OverviewPageShop(driver)
    shop.set_cookie_policy()
    shop.wait()
    txt = shop.Equal()
    assert txt == 'Total: $58.29', 'Error!'