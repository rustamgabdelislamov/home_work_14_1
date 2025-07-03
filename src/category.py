from src.product import Product


class Category:
    category_count = 0
    products_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products_list = products if products else []
        Category.category_count += 1
        Category.products_count += len(products) if products else 0

    def __str__(self):
        products_quantity = 0
        for product in self.__products_list:
            products_quantity += product.quantity
        return f"{self.name}, количество продуктов: {products_quantity} шт."

    @property
    def products(self):
        return self.__products_list

    @property
    def products_list(self):
        products_str = ''
        for product in self.__products_list:
            products_str += f'{str(product)}\n'
        return f"{products_str}"

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self.__products_list.append(product)

    @products_list.setter
    def products_list(self, new_product: Product):
        """сеттер, добавляющий в __products новый продукт с помощью метода add_product"""
        self.add_product(new_product)
        Category.products_count += 1

