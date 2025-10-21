import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# Тесты для capitalize()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("sakura", "Sakura"),
    ("Сакура", "Сакура"),
    ("сакура2025", "Сакура2025"),
    ("сакура", "Сакура"),
    ("цветение вишни", "Цветение вишни"),
    ("сакура!", "Сакура!")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123сакура", "123сакура"),
    ("", ""),
    (" ", " "),
    ("!@#$%", "!@#$%"),
    ("123 456", "123 456"),
    ("сАКУРА", "Сакура"),
    ("САКУРА", "Сакура"),
    ("сакура🌸", "Сакура🌸")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Тесты для trim()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" sakura", "sakura"),
    ("  цветение вишни", "цветение вишни"),
    ("   сакура  ", "сакура  "),
    ("  123", "123"),
    (" !Сакура!", "!Сакура"),
    (" сакура2025", "сакура2025")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
    ("цветение вишни", "цветение вишни"),
    ("сак ура", "сак ура"),
    ("сакура", "сакура"),
    ("sakura", "sakura"),
    ("\t\tspaces", "\t\tspaces"),  # Табуляция не удаляется
    ("\nnewline", "\nnewline")    # Новая строка не удаляется
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Тесты для contains()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("Сакура", "у", True),
    ("12345", "5", True),
    ("!@#$%", "#", True),
    ("aaaaaa", "a", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
    ("сакура", "", False),
    ("сакура", "Щ", False),  # Проверка регистрозависимости
    ("123", "4", False)
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


# Тесты для delete_symbol()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("Сакура", "у", "Сакра"),
    ("123123", "1", "2323"),
    ("цветение вишни", " ", "цветениевишни"),
    ("@#$%", "$", "@#%")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "a", ""),
    ("сакура", "", "сакура"),
    ("sakura", "x", "sakura"),
    ("aaaa", "a", ""),
    ("12345", "6", "12345")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
