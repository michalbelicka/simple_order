from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

BASE_URL = os.getenv(
    "SELENIUM_BASE_URL",
    "https://belicka-orders-api.onrender.com/"
)

def test_selenium_api():

    service = Service(ChromeDriverManager().install())
    options = Options()

    options.add_argument("--headless=new") 
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 60)

    driver.get(BASE_URL)

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
    driver.execute_script("arguments[0].click();", submit)

    h3_element = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Objednávka úspešne odoslaná!"))
    assert h3_element

    order_id_elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='order-id']")))
    order_id = order_id_elem.text

    assert order_id.startswith("#")
    assert order_id[1:].isdigit()

    new_order_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Vytvoriť novú objednávku")))
    new_order_link.click()

    wait.until(EC.visibility_of_element_located((By.ID, "name")))
    
    driver.quit()


    