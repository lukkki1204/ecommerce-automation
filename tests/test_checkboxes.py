import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkbox_click(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkbox1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//input[@type='checkbox'])[1]"))
    )

    if not checkbox1.is_selected():
        checkbox1.click()

    assert checkbox1.is_selected()

    checkbox2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//input[@type='checkbox'])[1]"))
    )

    if not checkbox2.is_selected():
        checkbox2.click()
    assert checkbox2.is_selected