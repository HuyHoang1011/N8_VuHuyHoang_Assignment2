import pytest
import time

from selenium.common import TimeoutException
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


def test_valid_keyword_search(driver):
    # Access the main page
    driver.get("http://localhost/OOAD/")

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

    # Perform login
    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập")))
    login_link.click()
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='login()']")))
    login_button.click()
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    username_field.send_keys("hoang@gmail.com")
    password_field.send_keys("huyhoang.1011")
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "xulydn")))
    submit_button.click()

    # Handle the login success alert
    try:
        alert = wait.until(EC.alert_is_present())
        print("Alert xuất hiện:", alert.text)  # Print the content of the alert to verify
        alert.accept()  # Close the alert
        print("Đã đóng alert đăng nhập thành công.")
    except:
        print("Không có alert đăng nhập thành công.")

    # Navigate to the "Trang Chủ" section
    home_page_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Trang Chủ")))
    home_page_link.click()
    wait.until(EC.url_contains("index.php"))
    print("Navigated to the home page.")

    # Navigate to the product page
    product_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sản Phẩm")))
    product_page.click()
    wait.until(EC.url_contains("index.php?action=productclassification"))
    print("Truy cập vào trang Sản Phẩm thành công.")

    # Enter the search keyword in the search bar
    search_bar = wait.until(EC.visibility_of_element_located((By.NAME, "namesp")))
    search_bar.clear()
    search_keyword = "adidas"
    search_bar.send_keys(search_keyword)

    # Click the search button to submit the search
    search_button = wait.until(EC.element_to_be_clickable((By.NAME, "search")))
    search_button.click()

    # Verify that the search results contain relevant products
    search_results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='col-4']/h4")))

    # Filter and validate that each relevant product contains the search keyword
    invalid_results = []  # To store any non-matching results
    for result in search_results:
        product_name = result.text
        print(f"Found product: {product_name}")
        if search_keyword.lower() not in product_name.lower():
            invalid_results.append(product_name)

    # Assert that no invalid results were found
    assert not invalid_results, f"Found non-matching products in search results: {invalid_results}"

    print("Valid keyword search test passed with only relevant products displayed.")

    # Pause for 10 seconds after search results are verified
    time.sleep(10)

def test_search_with_invalid_keyword(driver):
    # Access the main page
    driver.get("http://localhost/OOAD/")

    # Initialize WebDriverWait with a longer timeout
    wait = WebDriverWait(driver, 15)  # Increase wait time to 15 seconds

    # Perform login
    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập")))
    login_link.click()
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='login()']")))
    login_button.click()
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    username_field.send_keys("hoang@gmail.com")
    password_field.send_keys("huyhoang.1011")
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "xulydn")))
    submit_button.click()

    # Handle the login success alert
    try:
        alert = wait.until(EC.alert_is_present())
        print("Alert xuất hiện:", alert.text)
        alert.accept()
        print("Đã đóng alert đăng nhập thành công.")
    except:
        print("Không có alert đăng nhập thành công.")

    # Navigate to the product page
    product_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sản Phẩm")))
    product_page.click()
    wait.until(EC.url_contains("index.php?action=productclassification"))
    print("Truy cập vào trang Sản Phẩm thành công.")

    # Enter an invalid search keyword in the search bar
    search_bar = wait.until(EC.visibility_of_element_located((By.NAME, "namesp")))
    search_bar.clear()
    invalid_search_keyword = "shirt"
    search_bar.send_keys(invalid_search_keyword)

    # Click the search button to submit the search
    search_button = wait.until(EC.element_to_be_clickable((By.NAME, "search")))
    search_button.click()

    # Add a short delay to ensure the page has time to load
    time.sleep(2)

    try:
        no_results_container = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "row1"))
        )
        print("The 'No products found' container is displayed as expected.")
    except TimeoutException:
        print("Timeout: 'No products found' container was not displayed for an invalid keyword search.")
        raise AssertionError("Expected 'No products found' container not displayed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

        # Optional: Pause for 10 seconds to visually inspect the results
    time.sleep(10)


def test_case_insensitive_search(driver):
    # Access the main page
    driver.get("http://localhost/OOAD/")

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

    # Perform login
    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập")))
    login_link.click()
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='login()']")))
    login_button.click()
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    username_field.send_keys("hoang@gmail.com")
    password_field.send_keys("huyhoang.1011")
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "xulydn")))
    submit_button.click()

    # Handle the login success alert
    try:
        alert = wait.until(EC.alert_is_present())
        print("Alert xuất hiện:", alert.text)  # Print the content of the alert to verify
        alert.accept()  # Close the alert
        print("Đã đóng alert đăng nhập thành công.")
    except:
        print("Không có alert đăng nhập thành công.")

    # Navigate to the product page
    product_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sản Phẩm")))
    product_page.click()
    wait.until(EC.url_contains("index.php?action=productclassification"))
    print("Truy cập vào trang Sản Phẩm thành công.")

    # Function to perform search and return results
    def perform_search(keyword):
        search_bar = wait.until(EC.visibility_of_element_located((By.NAME, "namesp")))
        search_bar.clear()
        search_bar.send_keys(keyword)
        search_button = wait.until(EC.element_to_be_clickable((By.NAME, "search")))
        search_button.click()

        # Retrieve and store all product names in results
        search_results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='col-4']/h4")))
        return [result.text for result in search_results]

    # Perform searches with different cases
    lowercase_results = perform_search("adidas")
    print("Lowercase 'adidas' search results:", lowercase_results)
    time.sleep(2)  # Short pause between searches

    uppercase_results = perform_search("Adidas")
    print("Uppercase 'Adidas' search results:", uppercase_results)

    # Compare results
    assert lowercase_results == uppercase_results, "Search results differ between 'adidas' and 'Adidas'"

    print("Case insensitivity test passed: both searches returned the same results.")
    time.sleep(10)  # Pause for inspection
