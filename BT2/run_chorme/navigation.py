import time

from selenium.common import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import Select


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

def handle_alert_if_present(driver):
    """Đóng alert nếu có."""
    try:
        alert = driver.switch_to.alert
        print("Alert Text:", alert.text)  # Log alert text for verification
        alert.accept()  # Đóng alert
        print("Alert closed.")
    except NoAlertPresentException:
        pass  # Không có alert, tiếp tục

def test_homepage_navigation(driver):
    # Truy cập vào trang chính
    driver.get("http://localhost/OOAD/")

    # Khởi tạo WebDriverWait
    wait = WebDriverWait(driver, 10)  # Chờ tối đa 10 giây

    # Thực hiện đăng nhập
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

    # Xử lý alert "Dang nhap thanh cong" nếu có
    handle_alert_if_present(driver)

    # Kiểm tra khả năng truy cập từng trang trong menu
    try:
        # Truy cập trang Sản Phẩm
        product_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sản Phẩm")))
        product_page.click()
        wait.until(EC.url_contains("index.php?action=productclassification"))
        print("Truy cập vào trang Sản Phẩm thành công.")

        # Truy cập trang Bảo Hành
        warranty_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Bảo Hành")))
        warranty_page.click()
        wait.until(EC.url_contains("index.php?action="))  # Điều chỉnh nếu URL khác
        print("Truy cập vào trang Bảo Hành thành công.")

        # Truy cập trang Liên Hệ
        contact_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Liên Hệ")))
        contact_page.click()
        wait.until(EC.url_contains("index.php?action=contact"))
        print("Truy cập vào trang Liên Hệ thành công.")

        # Truy cập trang Giới Thiệu
        about_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Giới Thiệu")))
        about_page.click()
        wait.until(EC.url_contains("index.php?action="))  # Điều chỉnh nếu URL khác
        print("Truy cập vào trang Giới Thiệu thành công.")

        print("Tất cả các trang trong menu đều truy cập thành công.")
    except TimeoutException as e:
        print("Test thất bại: Không truy cập được một trong các trang trong menu.")
        print("Chi tiết lỗi:", e)

def test_category_navigation(driver):
    # Truy cập vào trang chính
    driver.get("http://localhost/OOAD/")

    # Khởi tạo WebDriverWait
    wait = WebDriverWait(driver, 10)  # Chờ tối đa 10 giây

    # Thực hiện đăng nhập
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

    # Xử lý alert đăng nhập thành công
    try:
        alert = wait.until(EC.alert_is_present())
        print("Alert xuất hiện:", alert.text)  # In nội dung của alert để xác minh
        alert.accept()  # Đóng alert
        print("Đã đóng alert đăng nhập thành công.")
    except:
        print("Không có alert đăng nhập thành công.")

    # Truy cập vào trang Sản Phẩm
    product_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sản Phẩm")))
    product_page.click()
    wait.until(EC.url_contains("index.php?action=productclassification"))
    print("Truy cập vào trang Sản Phẩm thành công.")

    # Chọn danh mục "ADIDAS" trong bộ lọc
    select_element = wait.until(EC.visibility_of_element_located((By.ID, "phanloai")))
    select = Select(select_element)  # Sử dụng Select từ Selenium
    select.select_by_value("ADIDAS")
    print("Đã chọn danh mục ADIDAS trong bộ lọc.")

    # Chờ cho các sản phẩm được lọc hiển thị
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.col-4 h4")))

    # Kiểm tra từng sản phẩm trong danh sách để đảm bảo rằng tất cả đều thuộc danh mục ADIDAS
    product_elements = driver.find_elements(By.CSS_SELECTOR, "div.col-4 h4")
    for _ in range(len(product_elements)):
        # Lấy lại danh sách sản phẩm mỗi lần duyệt để tránh lỗi stale element
        products = driver.find_elements(By.CSS_SELECTOR, "div.col-4 h4")
        product_name = products[_].text.upper()  # Chuyển tên sản phẩm thành chữ hoa để so sánh
        print(f"Tên sản phẩm: {product_name}")
        assert "ADIDAS" in product_name, f"Test failed: Sản phẩm không thuộc danh mục ADIDAS - {product_name}"

    print("Tất cả sản phẩm hiển thị đều thuộc danh mục ADIDAS. Test passed.")

def test_product_detail_navigation(driver):
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
        print("Alert appeared:", alert.text)  # Print the content of the alert to verify
        alert.accept()  # Close the alert
        print("Closed login success alert.")
    except:
        print("No login success alert appeared.")

    # Navigate to the product page
    product_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sản Phẩm")))
    product_page.click()
    wait.until(EC.url_contains("index.php?action=productclassification"))
    print("Successfully navigated to the product page.")

    # Click on the first product to view its details
    first_product_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-4']/a[@href='index.php?id=1&action=detail']")))
    first_product_link.click()

    # Verify that the URL contains the correct product detail page for the first product
    wait.until(EC.url_contains("index.php?id=1&action=detail"))
    current_url = driver.current_url
    assert current_url == "http://localhost/OOAD/index.php?id=1&action=detail", "Failed to navigate to the correct product detail page."

    print("Product detail navigation test passed.")

def test_cart_navigation(driver):
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
        print("Alert appeared:", alert.text)  # Print the content of the alert to verify
        alert.accept()  # Close the alert
        print("Closed login success alert.")
    except:
        print("No login success alert appeared.")

    # Navigate to the product page
    product_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sản Phẩm")))
    product_page.click()
    wait.until(EC.url_contains("index.php?action=productclassification"))
    print("Successfully navigated to the product page.")

    # Click on the second product to view its details (Adidas EQT Boost)
    second_product_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-4']/a[@href='index.php?id=2&action=detail']")))
    second_product_link.click()

    # Verify that the URL contains the correct product detail page for the second product
    wait.until(EC.url_contains("index.php?id=2&action=detail"))
    current_url = driver.current_url
    assert current_url == "http://localhost/OOAD/index.php?id=2&action=detail", "Failed to navigate to the correct product detail page."

    # Select size 38
    size_dropdown = wait.until(EC.element_to_be_clickable((By.NAME, "size")))
    size_dropdown.click()

    size_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name='size']/option[text()='39']")))
    size_option.click()

    # Select color Red
    color_dropdown = wait.until(EC.element_to_be_clickable((By.NAME, "color")))
    color_dropdown.click()

    color_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name='color']/option[text()='Red']")))
    color_option.click()

    # Add to cart
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Thêm vào giỏ hàng' and @name='add_card']")))
    add_to_cart_button.click()

    # Verify redirection to the cart page
    wait.until(EC.url_contains("index.php?action=cart"))
    assert driver.current_url == "http://localhost/OOAD/index.php?action=cart", "Failed to navigate to the cart page."

    # Verify that the cart contains the correct product details
    cart_product_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='cart-info']//p[text()='Adidas EQT Boost']")))
    cart_product_size = wait.until(EC.visibility_of_element_located((By.XPATH, "//td/div[@class='productSize' and text()='39']")))
    cart_product_color = wait.until(EC.visibility_of_element_located((By.XPATH, "//td/div[@class='productColor' and text()='Red']")))
    cart_product_price = wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text()='2.600.000 VNĐ']")))

    # Assert that all elements are correctly found
    assert cart_product_name is not None, "Product name not found in cart."
    assert cart_product_size is not None, "Product size not found in cart."
    assert cart_product_color is not None, "Product color not found in cart."
    assert cart_product_price is not None, "Product price not found in cart."

    print("Cart navigation test passed with correct product details.")