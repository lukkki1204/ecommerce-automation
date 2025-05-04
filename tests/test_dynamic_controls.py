from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_controls(driver):
    # First test Remove
    # Define the website
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    # Select "Remove" button
    remove = driver.find_element(By.XPATH, "//button[text()='Remove']")
    remove.click()

    # Define "Add" button
    add = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add']"))
    )

    # Validate if "Remove" button works
    assert add.is_displayed(), "Button is not visible"

    message1 = driver.find_element(By.ID, "message")

    assert message1.text == "It's gone!", "Unexpected message"

    # Second test - Enable
    # Select "Enable" button
    enable = driver.find_element(By.XPATH, "//button[text()='Enable']")
    enable.click()

    # Check if "Enable" is selected by checking if proper putton is displayed and text
    disable = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Disable']"))
    )
    assert disable.is_displayed(), "Disable buton is not visible"

    message2 = driver.find_element(By.ID, "message")
    assert message2.text == "It's enabled!", "Unexpected message"

    # Third test - Add 
    # Select add button
    add_new = driver.find_element(By.XPATH, "//button[text()='Add']")
    add_new.click()

    # Validate if its selected
    remove_new = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Remove']"))
    )
    assert remove_new.is_displayed(), "Button is not visible"

    message3 = driver.find_element(By.ID, "message")
    assert message3.text == "It's back!", f"Unexpected message {message3.text}"

    #Fourth test - disable
    # Now select disable
    disable_new = driver.find_element(By.XPATH, "//button[text()='Disable']")
    disable_new.click()

    # Validate if its selected
    enable_new = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Enable']"))
    )
    assert enable_new.is_displayed(), "Button not displayed"

    message4 = driver.find_element(By.ID, "message")
    assert message4.text == "It's disabled!"

