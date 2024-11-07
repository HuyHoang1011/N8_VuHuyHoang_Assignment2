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

def test_valid_registration(driver):
    # Truy cập vào trang đăng ký
    driver.get("http://localhost/OOAD/")  # Địa chỉ trang đăng ký

    # Khởi tạo WebDriverWait
    wait = WebDriverWait(driver, 10)  # Chờ tối đa 10 giây


    # Nhấp vào liên kết Đăng nhập để chuyển đến trang đăng ký
    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập")))
    login_link.click()

    # Điền thông tin vào các trường trong form đăng ký
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "user")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "pass")))
    confirm_password_field = wait.until(EC.visibility_of_element_located((By.ID, "pass")))
    fullname_field = wait.until(EC.visibility_of_element_located((By.ID, "name")))
    address_field = wait.until(EC.visibility_of_element_located((By.ID, "address")))
    phone_field = wait.until(EC.visibility_of_element_located((By.ID, "phone")))

    # Nhập các thông tin hợp lệ
    username_field.send_keys("hoangnguyen123@gmail.com")  # Tên tài khoản hợp lệ
    wait = WebDriverWait(driver, 10)
    password_field.send_keys("your_password")  # Mật khẩu hợp lệ
    wait = WebDriverWait(driver, 10)
    confirm_password_field.send_keys("your_password")  # Xác nhận mật khẩu khớp
    wait = WebDriverWait(driver, 10)
    fullname_field.send_keys("Vũ Huy Hoàng")  # Họ và tên hợp lệ
    wait = WebDriverWait(driver, 10)
    address_field.send_keys("123 Đường ABC, Quận 1, TP.HCM")  # Địa chỉ hợp lệ
    wait = WebDriverWait(driver, 10)
    phone_field.send_keys("0333456789")  # Số điện thoại hợp lệ
    wait = WebDriverWait(driver, 10)

    # Nhấp vào nút đăng ký
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "xulydk")))
    submit_button.click()

    # Kiểm tra alert đăng ký thành công
    try:
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text  # Lấy nội dung từ alert
        print(alert_text)  # In nội dung alert để kiểm tra
        assert alert_text == "Đăng kí thành công!"
        alert.accept()  # Nhấn OK để đóng alert
        print("Đăng ký thành công với dữ liệu hợp lệ.")
    except:
        print("Không thấy thông báo đăng ký thành công hoặc có lỗi trong quá trình đăng ký.")

def test_invalid_registration(driver):
    # Truy cập vào trang chính
    driver.get("http://localhost/OOAD/")  # Địa chỉ trang đăng ký

    # Khởi tạo WebDriverWait
    wait = WebDriverWait(driver, 10)  # Chờ tối đa 10 giây

    # Nhấp vào liên kết Đăng nhập để chuyển đến trang đăng ký
    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập")))
    login_link.click()

    # Điền thông tin vào các trường trong form đăng ký với dữ liệu không hợp lệ
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "user")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "pass")))
    confirm_password_field = wait.until(EC.visibility_of_element_located((By.ID, "pass")))
    address_field = wait.until(EC.visibility_of_element_located((By.ID, "address")))
    phone_field = wait.until(EC.visibility_of_element_located((By.ID, "phone")))

    # Nhập các thông tin hợp lệ, nhưng để trống trường Họ và tên
    username_field.send_keys("hoanggmail.com")  # Email không hợp lệ (thiếu @)
    password_field.send_keys("huyhoang.123")  # Mật khẩu hợp lệ
    confirm_password_field.send_keys("huyhoang.123")  # Xác nhận mật khẩu khớp
    address_field.send_keys("123 Đường ABC, Quận 1, TP.HCM")  # Địa chỉ hợp lệ
    phone_field.send_keys("12345678")  # Số điện thoại không hợp lệ (chỉ có 8 số)

    # Nhấp vào nút đăng ký
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "xulydk")))
    submit_button.click()

    wait = WebDriverWait(driver, 10)

    # Kiểm tra thông báo lỗi cho trường Họ và tên bị để trống
    try:
        # Tìm thông báo lỗi bên dưới trường Họ và tên
        error_message = wait.until(EC.visibility_of_element_located((By.ID, "error3")))
        error_text = error_message.text  # Lấy nội dung từ thông báo lỗi
        print(error_text)  # In nội dung lỗi để kiểm tra
        assert error_text == "No name received", "Thông báo lỗi không như mong đợi khi trường Họ và tên để trống."
        print("Thông báo lỗi 'No name received' xuất hiện như mong đợi.")

    except:
        print("Không thấy thông báo lỗi khi trường Họ và tên để trống.")
        wait = WebDriverWait(driver, 10)
