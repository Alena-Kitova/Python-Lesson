from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

search_box = driver.find_element(By.CSS_SELECTOR, "input#username")
search_box.send_keys("tomsmith")

sleep(2)

search_box = driver.find_element(By.CSS_SELECTOR, "input#password")
search_box.send_keys("SuperSecretPassword!")

sleep(2)

button = driver.find_element(By.CSS_SELECTOR, "button.radius")
button.send_keys("Login")

button.click()

sleep(2)

element_present = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "flash"))
)

raw_text = element_present.text

sleep(5)

driver.quit()
