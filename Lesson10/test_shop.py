import pytest
from selenium import webdriver
from shop import ShopPage
import allure


@pytest.fixture()
def driver():
    """
    Создает экземпляр WebDriver, открывает браузер,
    и закрывает его по окончании.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Покупка товаров на сайте")
@allure.description("Тест, проверяющий добавление товаров в корзину "
                    "и оформление заказа.")
@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)
def test_shopping(driver):
    """
    Выполняет последовательность:
    1. Открывает сайт
    2. Авторизуется
    3. Добавляет товары в корзину
    4. Переходит в корзину
    5. Оформляет заказ
    6. Проверяет итоговую сумму
    """
    shop_page = ShopPage(driver)

    with allure.step("Открытие главной страницы магазина"):
        shop_page.open()

    with allure.step("Авторизация пользователя"):
        shop_page.authorization()

    with allure.step("Добавление товаров в корзину"):
        shop_page.add_to_cart()

    with allure.step("Переход в корзину"):
        shop_page.cart()

    with allure.step("Шаг 5: Начало оформления заказа"):
        shop_page.checkout_cart()

    with allure.step("Шаг 6: Заполнение данных для оформления заказа"):
        shop_page.checkout_page()

    with allure.step("Проверка итоговой суммы заказа"):

        total = shop_page.get_total_price()
        expected_total = 58.29
        assert abs(total - expected_total) < 0.01, \
            f"Ожидаемая сумма: {expected_total}, фактическая: {total}"
