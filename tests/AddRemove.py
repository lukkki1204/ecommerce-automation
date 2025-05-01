from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

#initialization of website instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#open the website by get method
driver.get("https://the-internet.herokuapp.com/")

#wait until button is visible
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text()='Add/Remove Elements']"))
)

#select it
button.click()

add_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text()='Add Element']"))
)

add_button.click()

delete_button = WebDriverWait(driver, 10). until(
    EC.element_to_be_clickable((By.XPATH, "//*[text()='Delete']"))
)

page_source = driver.page_source
if 'Delete' in page_source:
    print("Text palced on the website")
else:
    print("Text didn't appear")

time.sleep(10)



