import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def driver():
    service = Service()
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_shop(driver):
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.CSS_SELECTOR, '#user-name')
    username.send_keys("standard_user")

    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.CSS_SELECTOR, '#login-button')
    login_button.click()

    backpack = driver.find_element(By.CSS_SELECTOR,
                                   "#add-to-cart-sauce-labs-backpack")
    backpack.click()

    tshirt = driver.find_element(By.CSS_SELECTOR,
                                 "#add-to-cart-sauce-labs-bolt-t-shirt")
    tshirt.click()

    onesie = driver.find_element(By.CSS_SELECTOR,
                                 "#add-to-cart-sauce-labs-onesie")
    onesie.click()

    cart_badge = driver.find_element(By.CSS_SELECTOR,
                                     "#shopping_cart_container")
    cart_badge.click()

    checkout_button = driver.find_element(By.CSS_SELECTOR, "#checkout")
    checkout_button.click()

    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.send_keys("Алена")
    first_name.click()

    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.send_keys("Китова")
    last_name.click()

    postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    postal_code.send_keys("620105")

    continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
    continue_button.click()

    text_prise = driver.find_element(By.CSS_SELECTOR,
                                     "div.summary_total_label").text
    text_prise_value = float(text_prise.split("$")[1])
    print(text_prise)

    assert text_prise_value == 58.29
