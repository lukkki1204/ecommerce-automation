from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_menu_element(driver):

    driver.get("https://the-internet.herokuapp.com/shifting_content")

    # Select Menu Element
    button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Example 1: Menu Element']"))
    )
    button.click()