from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
import time

def test_add_element(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    # Kliknij w przycisk "Add Element"
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    add_button.click()

    # Sprawdź, czy przycisk "Delete" się pojawił
    delete_button = driver.find_element(By.XPATH, "//button[text()='Delete']")
    assert delete_button.is_displayed()

def test_remove_element(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    # Kliknij w przycisk "Add Element"
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    add_button.click()

    # Teraz kliknij w przycisk "Delete"
    delete_button = driver.find_element(By.XPATH, "//button[text()='Delete']")
    delete_button.click()

    # Sprawdź, czy przycisk "Delete" został usunięty
    with pytest.raises(Exception):
        driver.find_element(By.XPATH, "//button[text()='Delete']")




