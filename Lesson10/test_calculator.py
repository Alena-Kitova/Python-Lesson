import pytest
from selenium import webdriver
from calculator import CalculatorPage
import allure


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """

    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест калькулятора: сложение 7 + 8")
@allure.description("Проверяет корректность вычисления суммы "
                    "7 + 8 в медленном калькуляторе'")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    """
    Тест проверяет работу калькулятора с различными операциями:
    - Экземпляр веб-драйвера, предоставляемый фикстурой
    - Открытие страницы калькулятора
    - Ввод задержки
    - Выполнение арифметической операции
    - Проверка результата
    """

    calculator_page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calculator_page.open()

    with allure.step("Ввести задержку в поле '45'"):
        calculator_page.input_field()

    with allure.step("Выполнить вычисление 7 + 8"):
        calculator_page.calculator_button()

    with allure.step("Получить результат и проверить его равенство '15'"):
        result = calculator_page.get_result()
        assert result == "15", f"Ожидалось '15', получено '{result}'"
