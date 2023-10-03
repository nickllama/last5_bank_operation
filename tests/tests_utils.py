import pytest

from utils.utils import filter_and_sorting
from utils.utils import get_date
from utils.utils import mask_prepare_message_number
from utils.utils import mask_card_number
from utils.utils import mask_account_number
from utils.utils import prepare_user_message


# Пример тестовых данных
sample_data = [
    {"state": "EXECUTED", "date": "2022-01-01"},
    {"state": "EXECUTED", "date": "2021-12-31"},
    {"state": "CANCELED", "date": "2022-02-01"},
]

def test_filter_and_sorting():
    # Проверяем, что функция возвращает список
    result = filter_and_sorting(sample_data)
    assert isinstance(result, list)

    # Проверяем, что функция фильтрует только операции со статусом "EXECUTED"
    for item in result:
        assert item["state"] == "EXECUTED"

    # Проверяем, что операции отсортированы по убыванию даты
    dates = [item["date"] for item in result]
    assert dates == ["2022-01-01", "2021-12-31"]


# Тесты для функции get_date

def test_get_date_valid_format():
    # Проверка корректного формата даты
    date_str = "2023-08-15T12:34:56.789"
    expected_result = "15.08.2023"
    assert get_date(date_str) == expected_result


# Напишем тест, который проверит, что функция работает правильно
def test_mask_prepare_message_number():
    # Тест с отсутствующим сообщением (None)
    message = None
    expected_result = 'Личный счет'
    assert mask_prepare_message_number(message) == expected_result

def test_mask_card_number():
    # Тест с корректным номером карты
    number = "1234567890123456"
    expected_result = "1234 56** **** 3456"
    assert mask_card_number(number) == expected_result


def test_mask_account_number():
    # Тест с корректным номером счета (длина >= 4)
    number = "123456"
    expected_result = "**3456"
    assert mask_account_number(number) == expected_result


def test_prepare_user_message():
    # Тест с корректными данными
    item = {
        "date": "2023-08-15T14:30:00.000000",
        "description": "Перевод организации",
        "from": "Счет 1234567890",
        "to": "Счет 9876543210",
        "operationAmount": {
            "amount": "1000.00",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        }
    }
    expected_result = "15.08.2023 Перевод организации\nСчет **7890 -> Счет **3210\n1000.00 руб.\n"
    assert prepare_user_message(item) == expected_result

