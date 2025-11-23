from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def authorization(self):
        username = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#user-name')))
        username.send_keys("standard_user")

        password = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        password.send_keys("secret_sauce")

        login_button = (self.driver.find_element
                        (By.CSS_SELECTOR, '#login-button'))
        login_button.click()

    def add_to_cart(self):

        backpack = (self.driver.find_element
                    (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))
        backpack.click()

        tshirt = (self.driver.find_element
                  (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"))
        tshirt.click()
        onesie = (self.driver.find_element
                  (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"))
        onesie.click()

    def cart(self):

        cart_badge = (self.driver.find_element
                      (By.CSS_SELECTOR, "#shopping_cart_container"))
        cart_badge.click()

    def checkout_cart(self):
        checkout_button = (self.driver.find_element
                           (By.CSS_SELECTOR, "#checkout"))
        checkout_button.click()

    def checkout_page(self):
        first_name = self.driver.find_element(By.CSS_SELECTOR, "#first-name")
        first_name.send_keys("Алена")
        first_name.click()

        last_name = self.driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name.send_keys("Китова")
        last_name.click()

        postal_code = self.driver.find_element(By.CSS_SELECTOR, "#postal-code")
        postal_code.send_keys("620105")

        continue_button = (self.driver.find_element
                           (By.CSS_SELECTOR, "#continue"))
        continue_button.click()

    def get_total_price(self):
        text_price = self.driver.find_element(By.CSS_SELECTOR,
                                              ".summary_total_label").text
        print(text_price)
        price_value = float(text_price.split("$")[1])
        return price_value
