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

def test_verify_account_details(driver):
    driver.get("http://localhost/OOAD/")

    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

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

    try:
        alert = wait.until(EC.alert_is_present())
        print("Alert appeared:", alert.text)
        alert.accept()  # Close the alert
        print("Closed login success alert.")
    except:
        print("No login success alert appeared.")


    home_page_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Trang Chủ")))
    home_page_link.click()
    wait.until(EC.url_contains("index.php"))
    print("Navigated to the home page.")


    account_info_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Vũ Huy Hoàng")))
    account_info_link.click()
    wait.until(EC.url_contains("index.php?action=info"))
    print("Navigated to My Account section.")

    name_field = wait.until(EC.visibility_of_element_located((By.ID, "info-name")))
    phone_field = wait.until(EC.visibility_of_element_located((By.ID, "info-phone")))
    address_field = wait.until(EC.visibility_of_element_located((By.ID, "info-address")))


    assert name_field.get_attribute("value") == "Vũ Huy Hoàng", "Name does not match expected value."
    assert phone_field.get_attribute("value") == "0335487431", "Phone number does not match expected value."
    assert address_field.get_attribute("value") == "Tân phú ", "Address does not match expected value."

    print("Account details verification test passed.")

def test_verify_order_history(driver):

    driver.get("http://localhost/OOAD/")


    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds


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


    try:
        alert = wait.until(EC.alert_is_present())
        print("Alert appeared:", alert.text)
        alert.accept()  # Close the alert
        print("Closed login success alert.")
    except:
        print("No login success alert appeared.")


    home_page_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Trang Chủ")))
    home_page_link.click()
    wait.until(EC.url_contains("index.php"))
    print("Navigated to the home page.")


    account_info_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Vũ Huy Hoàng")))
    account_info_link.click()
    wait.until(EC.url_contains("index.php?action=info"))
    print("Navigated to My Account section.")


    order_management_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?action=listorder']")))
    order_management_link.click()
    wait.until(EC.url_contains("index.php?action=listorder"))
    print("Navigated to Order Management page.")

    order_table = wait.until(EC.visibility_of_element_located((By.XPATH, "//table/tbody")))
    orders = order_table.find_elements(By.TAG_NAME, "tr")[1:]  # Skip the header row

    assert len(orders) > 0, "No previous orders found in order history."

    for order in orders:
        columns = order.find_elements(By.TAG_NAME, "td")
        order_id = columns[1].text
        order_date = columns[2].text
        order_total = columns[3].text
        order_status = columns[5].text
        print(f"Order ID: {order_id}, Date: {order_date}, Total: {order_total}, Status: {order_status}")

    print("Order history verification test passed successfully.")

def test_verify_cart_data(driver):
    driver.get("http://localhost/OOAD/")

    wait = WebDriverWait(driver, 10)

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

    try:
        alert = wait.until(EC.alert_is_present())
        print("Alert appeared:", alert.text)
        alert.accept()  # Close the alert
        print("Closed login success alert.")
    except:
        print("No login success alert appeared.")

    home_page_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Trang Chủ")))
    home_page_link.click()
    wait.until(EC.url_contains("index.php"))
    print("Navigated to the home page.")

    cart_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?action=cart' and @class='btncart']")))
    cart_icon.click()
    wait.until(EC.url_contains("index.php?action=cart"))
    print("Navigated to the cart page.")

    expected_total = 0
    cart_items = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr[not(contains(@style, 'background'))]")))

    for item in cart_items:
        product_name = item.find_element(By.XPATH, ".//div[@class='cart-info']//p").text
        size = item.find_element(By.XPATH, ".//td/div[@class='productSize']").text
        color = item.find_element(By.XPATH, ".//td/div[@class='productColor']").text
        quantity = int(item.find_element(By.XPATH, ".//td/input[@type='text']").get_attribute("value"))
        unit_price_text = item.find_element(By.XPATH, ".//div[@class='cart-info']//small").text
        item_total_text = item.find_element(By.XPATH, ".//td[last()]").text

        unit_price = int(unit_price_text.split(": ")[1])
        item_total = int(item_total_text.replace(".", "").replace(" VNĐ", ""))

        calculated_item_total = unit_price * quantity
        assert calculated_item_total == item_total, f"Incorrect total for {product_name}: expected {calculated_item_total} but got {item_total}"

        expected_total += item_total

        print(f"Product: {product_name}, Size: {size}, Color: {color}, Quantity: {quantity}, Unit Price: {unit_price}, Item Total: {item_total}")

    cart_total_text = driver.find_element(By.XPATH, "//tfoot//td[last()]").text
    cart_total = int(cart_total_text.replace(".", "").replace(" VNĐ", ""))
    assert cart_total == expected_total, f"Cart total mismatch: expected {expected_total} but got {cart_total}"

    print("Cart verification test passed with correct quantities, prices, and total cost.")

    