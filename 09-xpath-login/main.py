from selenium import webdriver
from selenium.webdriver.common.by import By
from login_config import USERNAME, URL, PASSWORD
import os
import time

# To use local driver, we added this path to the env PATH
#driver_path = os.path.join("drivers", "msedgedriver.exe")
#os.environ["SE_DRIVER_MIRROR_URL"] = "https://msedgedriver.microsoft.com"

driver = webdriver.Edge()

driver.get(URL)
driver.maximize_window()
time.sleep(5)

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)

login_button = driver.find_element(By.XPATH, "//button[@id='submit']")
login_button.click()

time.sleep(10)
driver.quit()



