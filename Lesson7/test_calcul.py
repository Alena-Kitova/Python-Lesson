import pytest
from selenium import webdriver
from Lesson7.calculator import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.open()
    calculator_page.input_field()
    calculator_page.calculator_button()
    calculator_page.get_result()

    result = calculator_page.get_result()
    assert result == "15"
