import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service


@pytest.fixture
def driver():
    service = Service()
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_form(driver):
    (driver.get
     ("https://bonigarcia.dev/selenium-webdriver-java/data-types.html"))

    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

    first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
    last_name.send_keys("Петров")

    address_input = driver.find_element(By.CSS_SELECTOR, "[name='address']")
    address_input.send_keys("Ленина, 55-3")

    email_address = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
    email_address.send_keys("test@skypro.com")

    phone_number = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
    phone_number.send_keys("+7985899998787")

    city_name = driver.find_element(By.CSS_SELECTOR, "[name='city']")
    city_name.send_keys("Москва")

    country_name = driver.find_element(By.CSS_SELECTOR, "[name='country']")
    country_name.send_keys("Россия")

    job_position = driver.find_element(By.CSS_SELECTOR,
                                       "[name='job-position']")
    job_position.send_keys("QA")

    company_name = driver.find_element(By.CSS_SELECTOR, "[name='company']")
    company_name.send_keys("SkyPro")

    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    submit_button.click()

    zip_code = (driver.find_element(By.CSS_SELECTOR, "#zip-code").
                value_of_css_property("border-color"))

    assert zip_code == 'rgb(245, 194, 199)'

    fields = ["first-name", "last-name", "address", "city",
              "country", "e-mail", "phone", "job-position", "company"]

    for field in fields:
        field_element = wait.until(EC.visibility_of_element_located(
            (By.ID, field)))
        border_color = field_element.value_of_css_property("border-color")
        print(f'Поле {field} имеет цвет границы: {border_color}')

        assert border_color == "rgb(186, 219, 204)", \
            f"Поле {field} не подсвечено зеленым"
