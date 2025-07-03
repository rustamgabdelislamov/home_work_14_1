import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


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


@pytest.fixture
def smartphone1():
    return Smartphone("Samsung Galaxy S23 Ultra",
                      "256GB, Серый цвет, 200MP камера",
                      180000.0,
                      5,
                      95.5,
                      "S23 Ultra",
                      256,
                      "Серый")


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15",
                      "512GB, Gray space",
                      210000.0,
                      8,
                      98.2,
                      "15",
                      512,
                      "Gray space")


@pytest.fixture
def lawn_grass1():
    return LawnGrass("Газонная трава",
                     "Элитная трава для газона",
                     500.0,
                     20,
                     "Россия",
                     "7 дней",
                     "Зеленый")

@pytest.fixture
def lawn_grass2():
    return LawnGrass("Газонная трава 2",
                     "Выносливая трава",
                     450.0,
                     15,
                     "США",
                     "5 дней",
                     "Темно-зеленый")