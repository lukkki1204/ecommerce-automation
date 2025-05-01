import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    # Set Chrome options to make sure it's NOT headless
    options = webdriver.ChromeOptions()
    options.headless = False  # Make sure headless mode is off

    # Initialize Chrome, driver is controller of a browser using python, thanks to it we can manipulate websites, its an object 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_open_login_page(driver):
    #We are using get method to open website
    driver.get("https://demo.opencart.com/") 
    time.sleep(5)  # Wait 5 seconds to see the browser

    #We are defining checkbox by waiting until its visible 
    #EC is Expected Conditions it contains different conditions of waiting
    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.TAG_NAME, "input"))
    )
    checkbox.click()

    email_field = driver.find_element(By.NAME, "email")
    assert email_field.is_displayed()

    time.sleep(3)  # Wait before closing (so you can see the result)


