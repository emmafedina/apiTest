import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

# Test data for both positive and negative test cases
test_data = [
    ("standard_user", "secret_sauce", True),  # Valid login
    ("", "", False),  # Empty fields (negative)
    ("invalid_user", "secret_sauce", False),  # Incorrect username
    ("InVaLiD_uSeR", "secret_sauce", False),  # Mixed-case incorrect username
    ("very_long_username_that_exceeds_the_maximum_length_allowed_by_the_application",
     "secret_sauce", False),  # Very long username (negative)

]


@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    yield driver
    driver.quit()


@pytest.mark.parametrize("username, password, success", test_data)
def test_login(browser, username, password, success):
    browser.get("https://www.saucedemo.com/")

    # Find username and password
    username_field = browser.find_element(By.ID, "user-name")
    password_field = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.ID, "login-button")

    #fill in username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Click the login button
    login_button.click()

    # Print the page source for debugging
    print("Page Source:")
    print(browser.page_source)
    if success:
        # Check for successful login
        assert "products" in browser.page_source.lower()
    else:
        # Check for error message
        assert "error" in browser.page_source.lower()


if __name__ == "__main__":
    pytest.main()
