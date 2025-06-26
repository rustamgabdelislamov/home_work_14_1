import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


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
def first_category(first_product, second_product):
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


@pytest.fixture
def category():
    return Category(name="Test Category", description="Description of Test Category", products=[])


@pytest.fixture(autouse=True)
def reset_product_count():
    Category.products_count = 0  # Сбрасываем счетчик перед каждым тестом
    yield
    Category.products_count = 0  # Сбрасываем после теста (если необходимо)


@pytest.fixture
def product_iterator(first_category):
    return ProductIterator(first_category)
