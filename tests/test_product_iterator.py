import pytest


def test_iterator(product_iterator):
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Infinix"
    assert next(product_iterator).name == "Samsung"

    with pytest.raises(StopIteration):
        next(product_iterator)