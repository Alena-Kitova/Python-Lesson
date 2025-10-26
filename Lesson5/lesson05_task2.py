from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid")
sleep(5)

blue_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
blue_button.send_keys("Button with Dynamic ID")
sleep(5)

blue_button.send_keys(Keys.RETURN)

driver.quit()
