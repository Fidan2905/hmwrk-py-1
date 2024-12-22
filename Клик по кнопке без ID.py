from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")


def test_dynamic_button():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get("http://uitestingplayground.com/dynamicid")

        button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")

        button.click()

        print("Кнопка успешно нажата.")

        time.sleep(2)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


test_dynamic_button()