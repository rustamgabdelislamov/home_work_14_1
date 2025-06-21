def test_category_init(first_category, second_category):
    """Тест инициализации категорий"""
    assert first_category.name == "Телефоны"
    assert first_category.description == "Современные телефоны"
    assert first_category.products_count == 4
    assert len(first_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2


def test_category_products_list_property(first_category):
    assert first_category.products_list == ('Infinix, 12GB, 12000 руб., Остаток: 5 шт. \n'
                                            'Samsung, 24GB, 22000 руб., Остаток: 3 шт. \n')


def test_category_products_list_setter(first_category, third_product):
    assert len(first_category.product_in_list) == 2
    first_category.products_list = third_product
    assert len(first_category.product_in_list) == 3
