from itertools import product

import pytest


from src.product import Product
from src.category import Category

def test_product_init(first_product):
    """Тест инициализации продуктов"""
    assert first_product.name == "Infinix"
    assert first_product.description == "12GB"
    assert first_product.price == 12000
    assert first_product.quantity == 5


def test_product_create():
    new_product = Product('Samsung','тел',10000, 5)
    new_product.name = 'Samsung'
    new_product.description = 'тел'
    new_product.price = 10000
    new_product.quantity = 5


def test_product_update_raise(first_product):
    with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
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




