from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


options = Options()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.ID, "ajaxButton")
button.click()

WebDriverWait(driver, 25).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "bg-success"))
    )
images = driver.find_element(By.CLASS_NAME, 'bg-success')
alert_text = images.text
print(alert_text)