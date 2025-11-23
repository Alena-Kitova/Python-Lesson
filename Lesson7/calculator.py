from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def input_field(self):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

    def calculator_button(self):
        button_7 = self.driver.find_element(By.XPATH, "//span[text()='7']")
        button_7.click()
        button_plus = self.driver.find_element(By.XPATH, "//span[text()='+']")
        button_plus.click()
        button_8 = self.driver.find_element(By.XPATH, "//span[text()='8']")
        button_8.click()
        button_equals = (self.driver.find_element
                         (By.XPATH, "//span[text()='=']"))
        button_equals.click()

    def get_result(self):
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), '15')
        )

        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result
