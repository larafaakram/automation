from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import os
import time


driver = webdriver.Edge()

driver.get(config.URL)
driver.maximize_window()

try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, 'firstname'))
    )

    driver.find_element(By.NAME, "firstname").send_keys(config.FORM_DATA["first_name"])
    driver.find_element(By.NAME, "lastname").send_keys(config.FORM_DATA["last_name"])
    print (config.FORM_DATA["first_name"])

    if config.FORM_DATA["gender"].lower() == "male":
        driver.find_element(By.ID, "sex-0").click()
    else:
        driver.find_element(By.ID, "sex-1").click()

    driver.find_element(By.ID, f"exp-{config.FORM_DATA['experience']}").click()
    driver.find_element(By.ID, "profession-0").click()
    driver.find_element(By.ID, "tool-2").click()
    driver.find_element(By.ID, "submit").click()

    time.sleep(30)

except Exception as e:
    print("Error:", e)

driver.quit()


