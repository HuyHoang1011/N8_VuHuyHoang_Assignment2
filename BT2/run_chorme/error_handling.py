import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_empty_fields_login(driver):
    driver.get("http://localhost/OOAD/")

    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập")))
    login_link.click()

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='login()']")))
    login_button.click()

    username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))

    username_field.send_keys("hoang@gmail.com")
    password_field.clear()

    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "xulydn")))
    submit_button.click()

    try:
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text  
        print(alert_text)
        assert alert_text == "Không được để trống", f"Unexpected alert message: '{alert_text}'"
        alert.accept()
        print("Empty fields login test passed.")
    except AssertionError as e:
        print(e)
        raise
    except:
        print("No alert appeared or unexpected behavior.")
        raise AssertionError("Expected alert with message 'Không được để trống' but none appeared.")

def test_register_with_duplicate_email(driver):
    # Access the registration page
    driver.get("http://localhost/OOAD/")  # Replace with the actual registration page URL if different

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

    # Click the login link to go to the registration page
    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập")))
    login_link.click()

    # Fill in the registration form fields
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "user")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "pass")))
    confirm_password_field = wait.until(EC.visibility_of_element_located((By.ID, "pass")))
    fullname_field = wait.until(EC.visibility_of_element_located((By.ID, "name")))
    address_field = wait.until(EC.visibility_of_element_located((By.ID, "address")))
    phone_field = wait.until(EC.visibility_of_element_located((By.ID, "phone")))

    # Input valid information with a duplicate email
    username_field.send_keys("hoang@gmail.com")  # Duplicate email
    password_field.send_keys("your_password")  # Valid password
    confirm_password_field.send_keys("your_password")  # Matching confirm password
    fullname_field.send_keys("Vũ Huy Hoàng")  # Valid full name
    address_field.send_keys("123 Đường ABC, Quận 1, TP.HCM")  # Valid address
    phone_field.send_keys("0333456789")  # Valid phone number

    # Click the Register button
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "xulydk")))
    submit_button.click()

    # Verify that an alert appears with the message "Đăng Kí Thất Bại"
    try:
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text  # Get the text from the alert
        print(alert_text)  # Print alert message for verification
        assert alert_text == "Đăng Kí Thất Bại", f"Unexpected alert message: '{alert_text}'"
        alert.accept()  # Close the alert
        print("Duplicate email registration test passed.")
    except AssertionError as e:
        print(e)
        raise  # Re-raise the assertion error to fail the test
    except:
        print("No alert appeared or unexpected behavior.")
        raise AssertionError("Expected alert with message 'Đăng Kí Thất Bại' but none appeared.")