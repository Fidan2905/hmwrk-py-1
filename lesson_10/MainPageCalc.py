from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPageCal:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get
        ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def set_cookie_policy(self):
        cookie = {"name": "cookie_policy", "value": "1"}
        self._driver.add_cookie(cookie)

    def wait_for_elements(self):
        WebDriverWait(self._driver, 25).until(
            EC.presence_of_all_elements_located((By.ID, "delay"))
        )

    def enter_time_delay(self, delay):
        input_field = self._driver.find_element(By.ID, "delay")
        input_field.clear()
        input_field.send_keys(delay)

    def enter_expression(self):
        self._click_button("7")
        self._click_button("+")
        self._click_button("8")
        self._click_button("=")

    def _click_button(self, button_text):
        button = self._driver.find_element
        (By.XPATH, f"//span[contains(.,'{button_text}')]")
        button.click()

    def get_result(self):
        WebDriverWait(self._driver, 46).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        return self._driver.find_element(By.CLASS_NAME, "screen").text