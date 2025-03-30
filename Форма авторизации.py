from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time

firefox_options = Options()
firefox_options.add_argument("--start-maximized")


def test_login():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

    try:
        driver.get("http://the-internet.herokuapp.com/login")

        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("tomsmith")
        print("Имя пользователя 'tomsmith' успешно введено.")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")
        print("Пароль успешно введен.")

        login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
        login_button.click()
        print("Кнопка 'Login' успешно нажата.")

        time.sleep(2)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


test_login()
