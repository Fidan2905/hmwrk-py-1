from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


options = Options()
options.add_argument('--ignore-certificate-errors')


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("http://uitestingplayground.com/textinput")


input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")


button = driver.find_element(By.ID, "updatingButton")
button.click()

button_text = button.text
print(button_text)

driver.quit()