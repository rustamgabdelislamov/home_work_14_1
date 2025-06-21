class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if new_price < self.__price:
            while True:  # Запрашиваем подтверждение до тех пор, пока не получим корректный ввод
                approval_input = input("Цена понижается!!! Снизить цену? (y - да, n - нет): ")
                if approval_input == 'y':
                    self.__price = new_price
                    print(f"Цена успешно снижена до {new_price}.")
                    break
                elif approval_input == 'n':
                    print("Цена осталась прежней.")
                    break
                else:
                    print("Некорректный ввод. Пожалуйста, введите 'y' или 'n'.")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data, category):
        """Добавляет новый продукт и проверяет есть ли такой продукт в списке"""
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']

        if category.products:  # Проверка, что список не пуст
            for existing_product in category.products:
                if existing_product.name == name:
                    existing_product.quantity += quantity
                    existing_product.price = price  # Устанавливаем цену напрямую
                    return
                    # Если мы нашли существующий продукт и обновили его количество и цену, выходим из метода.
                    # Здесь нет необходимости создавать новый продукт или добавлять его в категорию.

        new_product = Product(name, description, price, quantity)
        category.add_product(new_product)
