import json

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """Чтения файла json"""
    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def create_obj_from_json(data):
    """Функция автозаполнения из файла"""
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
        categories.append(Category(**category))

    return categories


if __name__ == '__main__':
    raw_data = read_json('../data/products.json')
    category_data = create_obj_from_json(raw_data)
    print(category_data[0].name)
    print(category_data[0].products)



