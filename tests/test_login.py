from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_open_login_page(driver):
    driver.get("https://example.com/login") 

    assert "Login" in driver.title  # Check if page contains "Login" word

def test_login(driver):
    driver.get("https://example.com/login") 

    # Find login fields
    username_field = driver.find_element(By.NAME, "username")  
    password_field = driver.find_element(By.NAME, "password")  

    username_field.send_keys("testuser")
    password_field.send_keys("password123")

    password_field.send_keys(Keys.RETURN)

    assert "Dashboard" in driver.title  
