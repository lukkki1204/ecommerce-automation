from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_open_login_page(driver):
    driver.get("https://example.com/login")  # Podmień na URL strony logowania

    assert "Login" in driver.title  # Sprawdza, czy tytuł strony zawiera słowo "Login"

def test_login(driver):
    driver.get("https://example.com/login")  # Podmień na URL strony logowania

    # Znajdź pola logowania (np. username i password)
    username_field = driver.find_element(By.NAME, "username")  # Zmienna zależna od strony
    password_field = driver.find_element(By.NAME, "password")  # Zmienna zależna od strony

    # Wprowadź dane logowania
    username_field.send_keys("testuser")
    password_field.send_keys("password123")

    # Zatwierdź formularz (np. klawiszem Enter)
    password_field.send_keys(Keys.RETURN)

    # Sprawdzenie, czy po zalogowaniu jesteśmy na stronie głównej lub innej stronie potwierdzającej logowanie
    assert "Dashboard" in driver.title  # Podmień na odpowiednią stronę po zalogowaniu
