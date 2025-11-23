import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Неявное ожидание элементов
    yield driver
    driver.quit()


def test_calc(driver):
    (driver.get
     ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"))

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
    button_7.click()
    button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
    button_plus.click()
    button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
    button_8.click()
    button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
    button_equals.click()

    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), '15')
    )

    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15"
