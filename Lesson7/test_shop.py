import pytest
from selenium import webdriver
from Lesson7.shop import ShopPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    shop_page = ShopPage(driver)
    shop_page.open()
    shop_page.authorization()
    shop_page.add_to_cart()
    shop_page.cart()
    shop_page.checkout_cart()
    shop_page.checkout_page()
    shop_page.get_total_price()

    total = shop_page.get_total_price()
    expected_total = 58.29
    assert abs(total - expected_total) < 0.01, \
        f"Ожидаемая сумма: {expected_total}, фактическая: {total}"
