from src.category import Category

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
                                            'Общее количество товаров: 8')


def test_category_products_list_setter(first_category, third_product):
    assert len(first_category.products) == 2  # Проверяем начальное количество продуктов
    first_category.products_list = third_product  # Используем сеттер для добавления продукта
    assert len(first_category.products) == 3  # Проверяем новое количество продуктов
    assert Category.products_count == 3  # Проверяем общий счетчик продуктов


def test_str(first_category):
    assert str(first_category) == "Телефоны, количество продуктов: 2 шт."





