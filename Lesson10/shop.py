from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ShopPage:
    """
    Класс, представляющий страницу интернет‑магазина.
    Содержит методы для авторизации, работы с корзиной и оформления заказа.
    """

    def __init__(self, driver):
        """
        Инициализация страницы магазина.
        :param driver:  WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу магазина")
    def open(self):
        """
        Открывает страницу магазина в браузере.
        Returns: None
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация пользователя")
    def authorization(self):
        """
        Выполняет авторизацию с предустановленными учетными данными:
        - логин: standard_user
        - пароль: secret_sauce
        Возвращает: None
        """

        username = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#user-name')))
        username.send_keys("standard_user")

        password = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        password.send_keys("secret_sauce")

        login_button = (self.driver.find_element
                        (By.CSS_SELECTOR, '#login-button'))
        login_button.click()

    @allure.step("Добавление товаров в корзину")
    def add_to_cart(self):
        """
        Добавляет в корзину три товара:
        - Sauce Labs Backpack
        - Sauce Labs Bolt T‑Shirt
        - Sauce Labs Onesie
        :return: None
        """

        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))).click()

        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"))).click()

    @allure.step("Переход в корзину")
    def cart(self):
        """
        Переходит в корзину через иконку корзины в шапке сайта.
        :return: None
        """

        cart_badge = (self.driver.find_element
                      (By.CSS_SELECTOR, "#shopping_cart_container"))
        cart_badge.click()

    @allure.step("Начало оформления заказа")
    def checkout_cart(self):
        """
        Нажимает кнопку «Checkout» для перехода к оформлению заказа.
        :return: None
        """

        checkout_button = (self.driver.find_element
                           (By.CSS_SELECTOR, "#checkout"))
        checkout_button.click()

    @allure.step("Заполнение данных для оформления заказа")
    def checkout_page(self):
        """
        Заполняет форму оформления заказа:
        - Имя
        - Фамилия
        - Почтовый индекс
        :return: None
        """

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

    @allure.step("Получение итоговой суммы заказа")
    def get_total_price(self) -> float:
        """
        Получает итоговую сумму заказа.
        Возвращает: float: сумма заказа.
        """

        text_price = self.driver.find_element(By.CSS_SELECTOR,
                                              ".summary_total_label").text
        print(text_price)
        price_value = float(text_price.split("$")[1])
        return price_value
