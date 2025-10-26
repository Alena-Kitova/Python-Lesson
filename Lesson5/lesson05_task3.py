from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")

search_box = driver.find_element(By.CSS_SELECTOR, "input")
search_box.send_keys("Sky")

sleep(5)

search_box.clear()

sleep(5)

search_box.send_keys("Pro")

sleep(5)

driver.quit()
