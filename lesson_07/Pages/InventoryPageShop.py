from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class InventoryPageShop:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/inventory.html")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def set_cookie_policy(self):
        cookie = {"name": "cookie_policy", "value": "1"}
        self._driver.add_cookie(cookie)

    def wait(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
            )
        )

    def additemintobasket(self):
        ID = "add-to-cart-sauce-labs-backpack"
        additem = self._driver.find_element(By.ID, ID)
        additem.click()
        ID = "add-to-cart-sauce-labs-bolt-t-shirt"
        additem = self._driver.find_element(By.ID, ID)
        additem.click()
        ID = "add-to-cart-sauce-labs-onesie"
        additem = self._driver.find_element(By.ID, ID)
        additem.click()
        ID = "shopping_cart_link"
        additem = self._driver.find_element(By.CLASS_NAME, ID)
        additem.click()