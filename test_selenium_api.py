from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import requests

def test_selenium_api():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    driver.get("http://127.0.0.1:5000")

    name = wait.until(EC.element_to_be_clickable((By.ID, "name")))
    name.send_keys("Tester")

    email = wait.until(EC.element_to_be_clickable((By.ID, "email")))
    email.send_keys("tester@example.com")

    address = wait.until(EC.element_to_be_clickable((By.ID, "address")))
    address.send_keys("TestingAddress")

    product = wait.until(EC.element_to_be_clickable((By.ID, "product")))
    product.send_keys("computer")

    quantity = wait.until(EC.element_to_be_clickable((By.ID, "quantity")))
    quantity.clear()
    quantity.send_keys("3")

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit.click()

    h1_flash = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    assert "Objednávka úspešne odoslaná!" in h1_flash.text

    driver.quit()

    response = requests.get("http://127.0.0.1:5000/orders")
    assert response.status_code == 200
    orders = response.json()
    assert any(
        order["name"] == "Tester" and 
        order["email"] == "tester@example.com" and
        order["address"] == "TestingAddress" and 
        order["product"] == "computer" and
        order["quantity"] == 3
        for order in orders
    )
    assert all(
    isinstance(order["id"], int) and
    isinstance(order["name"], str) and
    isinstance(order["email"], str) and
    isinstance(order["address"], str) and
    isinstance(order["product"], str) and
    isinstance(order["quantity"], int)
    for order in orders
    ), "Order 'Tester' not found in API response"