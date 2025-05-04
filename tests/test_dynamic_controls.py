from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_controls(driver):
    # Define the website
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    # Select "Remove" button
    remove = driver.find_element(By.NAME, "Remove")
    remove.click()

    # Define "Add" button
    add = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(By.NAME, "Add")
    )

    # Validate if "Remove" button works
    assert add.is_displayed(), "Button is not visible"
