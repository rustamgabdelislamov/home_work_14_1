def test_product_init(first_product):
    """Тест инициализации продуктов"""
    assert first_product.name == "Infinix"
    assert first_product.description == "12GB"
    assert first_product.price == 12000
    assert first_product.quantity == 5