from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

def test_entry_ad(driver):
    driver.get("https://the-internet.herokuapp.com/entry_ad")

    # Check if the popup is displayed
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal"))
    )
    assert modal.is_displayed(), "Modal is not displayed"

    close_button = driver.find_element(By.XPATH, "//div[@class='modal']//p[text()='Close']")
    close_button.click()

    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "modal"))
    )
    
    trigger_button = driver.find_element(By.ID, "restart-ad")
    trigger_button.click()

    assert modal.is_displayed(), "Modal is not displayed"

    close_button = driver.find_element(By.XPATH, "//div[@class='modal']//p[text()='Close']")
    close_button.click()

    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "modal"))
    )


