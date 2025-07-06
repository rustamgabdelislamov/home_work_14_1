from src.category import Category
from src.exceptions import ZeroQuantityProduct
from src.product import Product
import pytest

def test_category_init(first_category, second_category):
    """Тест инициализации категорий"""
    assert first_category.name == "Телефоны"
    assert first_category.description == "Современные телефоны"
    assert first_category.products_count == 4
    assert len(first_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2


def test_category_products_list_property(first_category):
    assert first_category.products_list == ('Infinix, 12000 руб. Остаток: 5 шт.\n'
                                            'Samsung, 22000 руб. Остаток: 3 шт.\n'
                                            )


def test_category_products_list_setter(first_category, third_product):
    assert len(first_category.products) == 2  # Проверяем начальное количество продуктов
    first_category.products_list = third_product  # Используем сеттер для добавления продукта
    assert len(first_category.products) == 3  # Проверяем новое количество продуктов
    assert Category.products_count == 3  # Проверяем общий счетчик продуктов


def test_str(first_category):
    assert str(first_category) == "Телефоны, количество продуктов: 8 шт."


def test_middle_price(first_category, second_without_category):
    assert first_category.middle_price() == 17000.0
    assert second_without_category.middle_price() == 0


def test_add_zero_quantity_product_raises_exception():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        product = Product(name="Infinix", description="12GB", price=12000, quantity=0)
