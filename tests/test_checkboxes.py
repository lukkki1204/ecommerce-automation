from selenium.webdriver.common.by import By

def test_checkbox_click(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkbox1 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]")
    checkbox2 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")

    if not checkbox1.is_selected():
        checkbox1.click()

    assert checkbox1.is_selected()

    if not checkbox2.is_selected():
        checkbox2.click()

    assert checkbox2.is_selected()