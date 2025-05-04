from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
import time

def test_add_element(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    # Select "Add Element" button
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    add_button.click()

    # Ckeck if "Delete" button appears
    delete_button = driver.find_element(By.XPATH, "//button[text()='Delete']")
    assert delete_button.is_displayed()

def test_remove_element(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    # Select "Add Element" button
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    add_button.click()

    # Select "Delete" button
    delete_button = driver.find_element(By.XPATH, "//button[text()='Delete']")
    delete_button.click()

    # Check if "Delete" has been removed
    with pytest.raises(Exception):
        driver.find_element(By.XPATH, "//button[text()='Delete']")




