from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get
("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


WebDriverWait(driver, 25).until(
        EC.presence_of_all_elements_located((By.ID, "award"))
    )

images = driver.find_element(By.ID, 'award')

src_value = images.get_attribute('src')
print(src_value)

driver.quit()
