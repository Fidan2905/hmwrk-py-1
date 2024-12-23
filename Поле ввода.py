from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time

firefox_options = Options()
firefox_options.add_argument("--start-maximized")


def test_input_field():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

    try:
        driver.get("http://the-internet.herokuapp.com/inputs")

        input_field = driver.find_element(By.TAG_NAME, "input")

        input_field.send_keys("1000")
        print("Текст '1000' успешно введен.")

        input_field.clear()
        print("Поле ввода успешно очищено.")

        input_field.send_keys("999")
        print("Текст '999' успешно введен.")

        time.sleep(2)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


test_input_field()
