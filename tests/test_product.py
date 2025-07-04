import pytest

from src.product import Product
from unittest.mock import Mock, patch


def test_product_init(first_product):
    """Тест инициализации продуктов"""
    assert first_product.name == "Infinix"
    assert first_product.description == "12GB"
    assert first_product.price == 12000
    assert first_product.quantity == 5


def test_product_create():
    new_product = Product('Samsung', 'тел', 10000, 5)
    new_product.name = 'Samsung'
    new_product.description = 'тел'
    new_product.price = 10000
    new_product.quantity = 5


def test_product_update_raise(first_product):
    with pytest.raises(ValueError, match="Цена не может быть отрицательной или равной нулю"):
        first_product.price = -10


def test_product_update_success(category):
    product1 = Product(
        name="Infinix",
        description="12GB",
        price=12000,
        quantity=5
    )
    category.add_product(product1)

    product2 = {
        'name': "Infinix",
        'description': "12GB",
        'price': 22000,
        'quantity': 5
    }

    Product.new_product(product2, category)

    assert product1.price == 22000


def test_str(first_product):
    assert str(first_product) == "Infinix, 12000 руб. Остаток: 5 шт."


def test_add(first_product, second_product):
    res = first_product + second_product
    assert res == 126000

@patch('builtins.input', return_value='y')
def test_price_update(mock_input):
    product = Product(name="Infinix", description="12GB", price=22000, quantity=5)
    product.price = 12000  # Понижаем цену
    assert product.price == 12000  # Проверяем, что цена изменилась корректно


@patch('builtins.input', return_value='n')
def test_price_update_no(mock_input):
    product = Product(name="Infinix", description="12GB", price=22000, quantity=5)
    product.price = 12000  # Понижаем цену
    assert product.price == 22000  # Проверяем, что цена изменилась корректно
