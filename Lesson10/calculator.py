from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """
    Класс, представляющий страницу калькулятора с медленным вычислением.
    """

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора в браузере.
        """

        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    @allure.step("Ввод задержки")
    def input_field(self):
        """
        Находит поле ввода задержки, очищает его и вводит значение '45'.
        :return: None
        """

        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

    @allure.step("Нажать кнопки и выполнить расчет")
    def calculator_button(self):
        """
        Выполняет последовательное нажатие кнопок калькулятора:
        7 + 8 =
        :return: None
        """
        button_7 = self.driver.find_element(By.XPATH, "//span[text()='7']")
        button_7.click()
        button_plus = self.driver.find_element(By.XPATH, "//span[text()='+']")
        button_plus.click()
        button_8 = self.driver.find_element(By.XPATH, "//span[text()='8']")
        button_8.click()
        button_equals = (self.driver.find_element
                         (By.XPATH, "//span[text()='=']"))
        button_equals.click()

    @allure.step("Получение результата")
    def get_result(self):
        """
        Ожидает появления результата в экране калькулятора
        и возвращает его текст.
        :return: Текст результата (тип: str)
        """

        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), '15')
        )

        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result
