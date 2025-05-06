from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_horizontal_slider(driver):
    driver.get("https://the-internet.herokuapp.com/horizontal_slider")

    slider = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )

    for _ in range(10):
        slider.send_keys(Keys.ARROW_RIGHT)
    
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.ID, "range"), "5")
    )

    value = driver.find_element(By.ID, "range").text
    assert value == "5"
    
