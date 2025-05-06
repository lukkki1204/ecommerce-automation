from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def test_exit_intent(driver):
    driver.get("https://the-internet.herokuapp.com/exit_intent")

    # Czekaj aż strona się załaduje — poczekaj na nagłówek H3: 'Exit Intent'
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h3"))
    )

    # Teraz możemy bezpiecznie działać dalej
    body = driver.find_element(By.TAG_NAME, "body")
    actions = ActionChains(driver)

    # Najpierw ustaw kursor na środek body
    actions.move_to_element_with_offset(body, 100, 100).perform()

    # Potem przesuń myszkę w górę (symuluje wyjście poza stronę)
    actions.move_by_offset(0, -195).perform()

    # Czekaj aż popup się pojawi
    modal = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal"))
    )

    # Kliknij w 'Close'
    close_button = modal.find_element(By.XPATH, ".//p[text()='Close']")
    close_button.click()

    # Poczekaj aż popup zniknie
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "modal"))
    )

    # Test przeszedł
    assert True
