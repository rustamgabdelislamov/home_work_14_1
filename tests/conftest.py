import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product(
        name="Infinix",
        description="12GB",
        price=12000,
        quantity=5
    )


@pytest.fixture
def second_product():
    return Product(
        name="Samsung",
        description="24GB",
        price=22000,
        quantity=3
    )


@pytest.fixture
def third_product():
    return Product(
        name="TCL",
        description="12GB",
        price=120000,
        quantity=4
    )


@pytest.fixture
def fourth_product():
    return Product(
        name="Samsung",
        description="12GB",
        price=220000,
        quantity=3
    )


@pytest.fixture
def first_category(first_product,second_product):
    return Category(
        name="Телефоны",
        description="Современные телефоны",
        products=[
            first_product, second_product]
    )


@pytest.fixture
def second_category(third_product, fourth_product):
    return Category(
        name="Телевизоры",
        description="Qled дисплеи",
        products=[third_product, fourth_product]
    )


