from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
WebDriverWait(driver, 25).until(
        EC.presence_of_all_elements_located((By.ID, "delay"))
    )


driver.find_element(By.ID, 'delay').clear()
input_field = driver.find_element(By.ID, 'delay')
input_field.send_keys("2")


keynums = driver.find_element(By.XPATH, "//span[contains(.,'7')]")
keynums.click()
keynums = driver.find_element(By.XPATH, "//span[contains(.,'+')]")
keynums.click()
keynums = driver.find_element(By.XPATH, "//span[contains(.,'8')]")
keynums.click()
keynums = driver.find_element(By.XPATH, "//span[contains(.,'=')]")
keynums.click()


WebDriverWait(driver, 45).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), '15'))
t = driver.find_element(By.CLASS_NAME, 'screen')


assert t.text == '15', 'Ожидалось значение 15'
