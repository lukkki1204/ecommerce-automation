from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def test_dropdown(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")

    # Find a dropdown
    dropdown = driver.find_element(By.ID, "dropdown")

    # Create select object
    select = Select(dropdown)

    # Select by visible text option 1
    select.select_by_visible_text("Option 1")

    # Validate if Option1 has been selected
    selected_option = select.first_selected_option
    assert selected_option.text == "Option 1"

    # Select by visible option 2
    select.select_by_visible_text("Option 2")

    # Validate if Option2 has been selected
    selected_option = select.first_selected_option
    assert selected_option.text == "Option 2"



