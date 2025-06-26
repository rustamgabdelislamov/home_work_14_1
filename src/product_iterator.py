from src.product import Product
from src.category import Category


class ProductIterator:
    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self


    def __next__(self):
        if self.index < len(self.category.products):
            product_ = self.category.products[self.index]
            self.index += 1
            return product_
        else:
            raise StopIteration

if __name__ == '__main__':
    product1 = Product('Samsung', 'тел', 10000, 5)
    product2 = Product('Lg', 'тел', 11000, 6)
    product3 = Product('Nokia', 'тел', 11000, 7)

    category = Category('тел', 'cool', [product1, product2, product3])

    product4 = Product('Moto', 'тел', 10000, 3)
    category.add_product(product4)
    print(product1)
    iterator = ProductIterator(category)
    for product in iterator:
        print(product)