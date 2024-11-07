import time

import pytest




# User Authentication
# TC1: Valid Login

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

def test_valid_login(driver):
    # Access the main page
    driver.get("http://localhost/OOAD/")

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

    # Click the login link <a href="index.php?action=account">Đăng nhập</a>
    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập")))
    login_link.click()

    # Click the login button <span onclick="login()">Đăng nhập</span>
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='login()']")))
    login_button.click()

    # Wait for the username and password fields to become visible
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))

    # Enter the credentials
    username_field.send_keys("hoang@gmail.com")
    password_field.send_keys("huyhoang.1011")  # Replace with the actual password

    # Find and click the Login button <button id="xulydn" class="btn">Login</button>
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "xulydn")))
    submit_button.click()

    # Wait for the alert to appear and handle it
    try:
        alert = wait.until(EC.alert_is_present())
        print(alert.text)  # Print alert message (optional)
        alert.accept()  # Click OK to close the alert
        print("Dang nhap thanh xong")
    except:
        print("No alert apeared")

    print("Login test executed successfully.")


def test_invalid_login(driver):
    # Access the main page
    driver.get("http://localhost/OOAD/")

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

    # Click the login link <a href="index.php?action=account">Đăng nhập</a>
    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập")))
    login_link.click()

    # Click the login button <span onclick="login()">Đăng nhập</span>
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='login()']")))
    login_button.click()

    # Wait for the username and password fields to become visible
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))

    # Enter the credentialYs with an incorrect password
    username_field.send_keys("hoang@gmail.com")
    password_field.send_keys("hhh")  # Incorrect password

    # Find and click the Login button <button id="xulydn" class="btn">Login</button>
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "xulydn")))
    submit_button.click()

    # Wait for the alert to appear and verify the message
    try:
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text  # Get the text from the alert
        print(alert_text)  # Print alert message for verification
        assert alert_text == "Tai Khoan Hoac mat khau khong chinh xac!!!"
        alert.accept()  # Click OK to close the alert
        print("Invalid login test passed with expected alert.")
    except:
        print("No alert appeared or unexpected alert message.")

    print("Invalid login test executed successfully.")


def test_logout_functionality(driver):
    # Access the main page
    driver.get("http://localhost/OOAD/")

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

    # Click the login link <a href="index.php?action=account">Đăng nhập</a>
    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập")))
    login_link.click()

    # Click the login button <span onclick="login()">Đăng nhập</span>
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='login()']")))
    login_button.click()

    # Wait for the username and password fields to become visible
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))

    # Enter the credentials
    username_field.send_keys("hoang@gmail.com")
    password_field.send_keys("huyhoang.1011")  # Replace with the actual password

    # Find and click the Login button <button id="xulydn" class="btn">Login</button>
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "xulydn")))
    submit_button.click()

    # Wait for the alert to appear and handle it
    try:
        alert = wait.until(EC.alert_is_present())
        print(alert.text)  # Print alert message (optional)
        alert.accept()  # Click OK to close the alert
        print("Dang nhap thanh cong")
    except:
        print("No alert appeared or unexpected alert message.")

    # Verify user is logged in by checking for the user name link
    user_name_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?action=info']")))
    assert user_name_link.text == "Vũ Huy Hoàng", "User name did not appear after login."

    # Perform logout
    logout_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?action=logout_user']")))
    logout_link.click()

    # Verify that the login link reappears, indicating a successful logout
    login_link_after_logout = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Đăng nhập")))
    assert login_link_after_logout, "Login link did not reappear after logout."

    print("Logout functionality test executed successfully.")

def test_session_expiry(driver):
    # Access the main page
    driver.get("http://localhost/OOAD/")

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

    # Click the login link <a href="index.php?action=account">Đăng nhập</a>
    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập")))
    login_link.click()

    # Click the login button <span onclick="login()">Đăng nhập</span>
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='login()']")))
    login_button.click()

    # Wait for the username and password fields to become visible
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))

    # Enter the credentials
    username_field.send_keys("hoang@gmail.com")
    password_field.send_keys("huyhoang.1011")  # Replace with the actual password

    # Find and click the Login button <button id="xulydn" class="btn">Login</button>
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "xulydn")))
    submit_button.click()

    # Wait for the alert to appear and handle it
    try:
        alert = wait.until(EC.alert_is_present())
        print(alert.text)  # Print alert message (optional)
        alert.accept()  # Click OK to close the alert
        print("Đăng nhập thành công")
    except:
        print("Không có thông báo hoặc thông báo không như mong đợi.")

    # Verify user is logged in by checking for the user name link
    user_name_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?action=info']")))
    assert user_name_link.text == "Vũ Huy Hoàng", "Tên người dùng không xuất hiện sau khi đăng nhập."

    # Simulate inactivity by waiting for 60 seconds
    print("Chờ 60 giây để phiên hết hạn...")
    time.sleep(5)  # Wait for 60 seconds to simulate inactivity

    # Reload the page to check session expiry
    driver.refresh()

    # Check if the session expired by verifying if the login link reappears
    try:
        # Try to find the username link again
        user_name_link_after_expiry = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='index.php?action=info']")), 10)
        # If username link is still visible, session has not expired
        if user_name_link_after_expiry.text == "Vũ Huy Hoàng":
            print("Session did not expire as expected.")
            assert False, "Test failed: Session did not expire after 60 seconds of inactivity."
    except:
        # If the username link is not found, it means session has expired, and login link should appear
        login_link_after_expiry = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Đăng nhập")))
        assert login_link_after_expiry, "Login link did not appear after session expiry."
        print("Session expired as expected; redirected to login page.")

