from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time

firefox_options = Options()
firefox_options.add_argument("--start-maximized")


def test_entry_ad_modal():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

    try:
        driver.get("http://the-internet.herokuapp.com/entry_ad")

        time.sleep(2)

        close_button = driver.find_element(By.CSS_SELECTOR, "#modal .modal-footer > p")
        close_button.click()

        print("Модальное окно успешно закрыто.")

        time.sleep(2)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


test_entry_ad_modal()
