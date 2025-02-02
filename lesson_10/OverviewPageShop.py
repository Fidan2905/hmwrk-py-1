from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class OverviewPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/checkout-step-two.html")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def set_cookie_policy(self):
        cookie = {"name": "cookie_policy", "value": "1"}
        self._driver.add_cookie(cookie)

    def wait(self):
        WebDriverWait(self._driver, 20).until(
            EC.presence_of_all_elements_located((By.ID, "finish"))
        )

    def Equal(self):
        total = self._driver.find_element(By.CLASS_NAME, "summary_total_label")
        toprint = total.text
        return toprint