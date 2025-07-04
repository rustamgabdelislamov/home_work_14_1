import pytest

from src.product import Product
from src.product_iterator import ProductIterator


def test_iterator(product_iterator):
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Infinix"
    assert next(product_iterator).name == "Samsung"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_full_iteration(product_iterator):
    products = [product.name for product in product_iterator]
    assert products == ["Infinix", "Samsung"]  # Убедитесь, что у вас правильные имена продуктов


def test_empty_category_iterator(category):
    empty_category = category
    iterator = ProductIterator(empty_category)
    with pytest.raises(StopIteration):
        next(iterator)


def test_iterator_return_type(product_iterator):
    product = next(product_iterator)
    assert isinstance(product, Product)
