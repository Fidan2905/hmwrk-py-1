from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPageShop:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def set_cookie_policy(self):
        cookie = {
            "name": "cookie_policy",
            "value": "1"
        }
        self._driver.add_cookie(cookie)

    def wait(self):
        WebDriverWait(self._driver, 25).until(EC.presence_of_all_elements_located((By.ID, "password")))

    def enterloginpass(self):
        input_field = self._driver.find_element(By.ID, 'user-name')
        input_field.send_keys("standard_user")
        input_field = self._driver.find_element(By.ID, 'password')
        input_field.send_keys("secret_sauce")
        presslogin = self._driver.find_element(By.ID, 'login-button')
        presslogin.click()
