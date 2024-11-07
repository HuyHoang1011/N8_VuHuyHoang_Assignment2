
import pytest
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_mobile_view_compatibility(driver):
    # Set the window size to a common mobile resolution (e.g., iPhone X dimensions)
    driver.set_window_size(375, 667)

    # Access the main page
    driver.get("http://localhost/OOAD/")

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

    # Ensure that menu items are hidden by default before clicking the menu icon
    try:
        nav_items = driver.find_elements(By.CLASS_NAME, "header_top")
        for item in nav_items:
            assert not item.is_displayed(), "Menu items are visible without clicking the menu icon."
        print("Menu items are hidden by default on mobile view.")
    except AssertionError:
        raise AssertionError("Test failed: Some menu items are visible without clicking the menu icon.")

    # Verify the navigation menu icon is visible and clickable
    try:
        menu_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "menu-icon")))
        assert menu_icon.is_displayed(), "Mobile menu icon is not visible on mobile view."
        print("Mobile menu icon is displayed correctly.")

        # Click the menu icon to open the navigation
        menu_icon.click()

        # Verify that the navigation items are now visible after clicking the icon
        nav_items = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header_top")))
        assert nav_items.is_displayed(), "Navigation items are not visible after clicking the mobile menu icon."
        print("Navigation items are displayed correctly on mobile view after clicking the menu icon.")
    except TimeoutException:
        raise AssertionError("Navigation menu is not functioning as expected on mobile view.")

    # Verify that the logo is visible and scaled properly
    try:
        logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header_top.logo img")))
        assert logo.is_displayed(), "Logo is not visible on mobile view."
        print("Logo is displayed correctly on mobile view.")
    except TimeoutException:
        raise AssertionError("Logo is not displayed correctly on mobile view.")

    # Verify that the featured products images are visible and responsive
    try:
        product_images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-img img")))
        for img in product_images:
            assert img.is_displayed(), "A product image is not visible on mobile view."
        print(f"All {len(product_images)} product images are displayed correctly on mobile view.")
    except TimeoutException:
        raise AssertionError("Product images are not displayed or responsive on mobile view.")

    # Verify that the search and cart icons are visible
    try:
        search_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header_top_1")))
        cart_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btncart")))
        assert search_icon.is_displayed(), "Search icon is not visible on mobile view."
        assert cart_icon.is_displayed(), "Cart icon is not visible on mobile view."
        print("Search and cart icons are displayed correctly on mobile view.")
    except TimeoutException:
        raise AssertionError("Search or cart icons are not displayed on mobile view.")

    # Verify that the footer is present and adapts to mobile view
    try:
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        assert footer.is_displayed(), "Footer is not visible on mobile view."
        print("Footer is displayed correctly on mobile view.")
    except TimeoutException:
        raise AssertionError("Footer is not displayed or responsive on mobile view.")

    # Optional: Pause to allow for manual inspection
    time.sleep(10)

    print("Mobile view compatibility test passed: All key elements are displayed and responsive on mobile view.")


def test_tablet_view_compatibility(driver):
    # Set the window size to a tablet resolution (e.g., iPad portrait dimensions)
    driver.set_window_size(768, 1024)

    # Access the main page
    driver.get("http://localhost/OOAD/")

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

    # Ensure that menu items are hidden by default before clicking the menu icon
    try:
        nav_items = driver.find_elements(By.CLASS_NAME, "header_top")
        for item in nav_items:
            assert not item.is_displayed(), "Menu items are visible without clicking the menu icon."
        print("Menu items are hidden by default on mobile view.")
    except AssertionError:
        raise AssertionError("Test failed: Some menu items are visible without clicking the menu icon.")

    # Verify the navigation menu icon is visible and clickable
    try:
        menu_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "menu-icon")))
        assert menu_icon.is_displayed(), "Mobile menu icon is not visible on mobile view."
        print("Mobile menu icon is displayed correctly.")

        # Click the menu icon to open the navigation
        menu_icon.click()

        # Verify that the navigation items are now visible after clicking the icon
        nav_items = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header_top")))
        assert nav_items.is_displayed(), "Navigation items are not visible after clicking the mobile menu icon."
        print("Navigation items are displayed correctly on mobile view after clicking the menu icon.")
    except TimeoutException:
        raise AssertionError("Navigation menu is not functioning as expected on mobile view.")

    # Verify that the logo is visible and scaled properly
    try:
        logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header_top.logo img")))
        assert logo.is_displayed(), "Logo is not visible on mobile view."
        print("Logo is displayed correctly on mobile view.")
    except TimeoutException:
        raise AssertionError("Logo is not displayed correctly on mobile view.")

    # Verify that the featured products images are visible and responsive
    try:
        product_images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-img img")))
        for img in product_images:
            assert img.is_displayed(), "A product image is not visible on mobile view."
        print(f"All {len(product_images)} product images are displayed correctly on mobile view.")
    except TimeoutException:
        raise AssertionError("Product images are not displayed or responsive on mobile view.")

    # Verify that the search and cart icons are visible
    try:
        search_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header_top_1")))
        cart_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btncart")))
        assert search_icon.is_displayed(), "Search icon is not visible on mobile view."
        assert cart_icon.is_displayed(), "Cart icon is not visible on mobile view."
        print("Search and cart icons are displayed correctly on mobile view.")
    except TimeoutException:
        raise AssertionError("Search or cart icons are not displayed on mobile view.")

    # Verify that the footer is present and adapts to mobile view
    try:
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        assert footer.is_displayed(), "Footer is not visible on mobile view."
        print("Footer is displayed correctly on mobile view.")
    except TimeoutException:
        raise AssertionError("Footer is not displayed or responsive on mobile view.")

    # Optional: Pause to allow for manual inspection
    time.sleep(10)

    print("Mobile view compatibility test passed: All key elements are displayed and responsive on mobile view.")
