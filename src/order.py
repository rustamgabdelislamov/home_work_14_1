from abc import ABC, abstractmethod
from src.product import Product


class BaseEntity(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_info(self):
        pass


class Order(BaseEntity):
    def __init__(self, product_, quantity):
        super().__init__(product_.name)
        self.product = product_
        self.quantity = quantity
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        return self.product.price * self.quantity

    def get_info(self):
        return (f"Заказ: {self.name}, "
                f"Количество: {self.quantity}, "
                f"Итоговая стоимость: {self.total_price:.2f}")
