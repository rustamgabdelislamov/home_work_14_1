def test_category_init(first_category, second_category):
    """Тест инициализации категорий"""
    assert first_category.name == "Телефоны"
    assert first_category.description == "Современные телефоны"
    assert first_category.products_count == 4
    assert len(first_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2
