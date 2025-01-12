from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPageForm:
    green_fields = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company",
        ]

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "http://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def set_cookie_policy(self):
        cookie = {"name": "cookie_policy", "value": "1"}
        self._driver.add_cookie(cookie)

    def waitbyname(self):
        WebDriverWait(self._driver, 25).until(
            EC.presence_of_all_elements_located((By.NAME, "company"))
        )

    def fill_form_element(self):
        self._driver.find_element(By.NAME, "first-name").send_keys("Иван")
        self._driver.find_element(By.NAME, "last-name").send_keys("Петров")
        self._driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        self._driver.find_element(By.NAME, "e-mail").send_keys("test@sky.com")
        self._driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        self._driver.find_element(By.NAME, "zip-code").send_keys("")
        self._driver.find_element(By.NAME, "city").send_keys("Москва")
        self._driver.find_element(By.NAME, "country").send_keys("Россия")
        self._driver.find_element(By.NAME, "job-position").send_keys("QA")
        self._driver.find_element(By.NAME, "company").send_keys("SkyPro")
        t = self._driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        t.click()

    def waitbyid(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "company"))
        )

    def assert_red(self):
        return self._driver.find_element(By.ID, "zip-code")

    def assert_green(self, elid):
        return self._driver.find_element(By.ID, elid)