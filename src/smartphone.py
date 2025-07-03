from src.product import Product

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


    def __add__(self, other):
        if type(other) is Smartphone:
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError


if __name__ == '__main__':
    sm1 = Smartphone('Samsung', 'тел', 10000, 5, "12 Gb", "S", "256", "Red")
    sm2 = Smartphone('Samsung', 'тел', 10000, 5, "12 Gb", "S", "256", "Red")
    print(sm1 + sm2)




