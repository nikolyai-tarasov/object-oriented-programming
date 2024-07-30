class Product:
    name: str
    description: str
    price: int
    quantity: int
    counter_of_all_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.counter_of_all_products += quantity

    @classmethod
    def new_product(cls, my_dict):
        name = my_dict["name"]
        description = my_dict["description"]
        price = my_dict["price"]
        quantity = my_dict["quantity"]
        instance = cls(name, description, price, quantity)
        return instance

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self):
        return f"{self.name}, {self.__price}. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.quantity * self.__price + other.quantity * other.__price
