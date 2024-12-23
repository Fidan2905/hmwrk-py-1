from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "password"))
    )


input_field = driver.find_element(By.ID, 'user-name')
input_field.send_keys("standard_user")
input_field = driver.find_element(By.ID, 'password')
input_field.send_keys("secret_sauce")


presslogin = driver.find_element(By.ID, 'login-button')
presslogin.click()


WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"))
    )


additem = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
additem.click()
additem = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
additem.click()
additem = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
additem.click()


additem = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
additem.click()


WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "checkout"))
    )


additem = driver.find_element(By.ID, 'checkout')
additem.click()


WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "continue"))
    )


additem = driver.find_element(By.ID, 'first-name')
additem.send_keys("Жирный")
additem = driver.find_element(By.ID, 'last-name')
additem.send_keys("Член")
additem = driver.find_element(By.ID, 'postal-code')
additem.send_keys("248000")
additem = driver.find_element(By.ID, 'continue')
additem.click()
WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.ID, "finish"))
    )


total = driver.find_element(By.CLASS_NAME, 'summary_total_label')
toprint = total.text
driver.quit()
print(toprint)

assert toprint != 'Total: $58.29', 'Тест прошел успешно'