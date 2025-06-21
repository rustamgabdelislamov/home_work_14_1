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

    @property
    def products(self):
        return self.__products_list

    @property
    def products_list(self):
        products_str = ''
        for product in self.__products_list:
            products_str += (f'{product.name}, {product.description}, {product.price} руб., '
                             f'Остаток: {product.quantity} шт. \n')
        return products_str

    @products_list.setter
    def products_list(self, new_product: Product):
        """сеттер, добавляющий в __products новый продукт с помощью метода add_product"""
        self.add_product(new_product)
        Category.products_count += 1

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self.__products_list.append(product)

    @property
    def product_in_list(self):
        return self.__products_list
