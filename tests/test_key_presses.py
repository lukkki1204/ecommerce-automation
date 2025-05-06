from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_key_presses(driver):
    driver.get("https://the-internet.herokuapp.com/key_presses?")

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )
    # In the loop test each alphabetic letter
    alphabet = "abcdefghijklmnoupqrstuvwxyz".upper()

    for i in alphabet:
        entry = driver.find_element(By.TAG_NAME, "input")

        entry.send_keys(i)

        response = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, "result"))
        )

        assert response.text == "You entered: " + i, "Incorrect input"

        entry.clear()