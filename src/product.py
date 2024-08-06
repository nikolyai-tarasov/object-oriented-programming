from src.base_product import BaseProduct
from src.mixin_log import MixinLog


class Product(MixinLog, BaseProduct):
    """Класс 'Product' создает экземпляры продуктов"""
    name: str
    description: str
    price: int
    quantity: int
    counter_of_all_products = 0

    def __init__(self, name, description, price, quantity):
        """Конструктор класса"""
        super().__init__(name, description, price, quantity)
        Product.counter_of_all_products += quantity
        super().__repr__()

    @classmethod
    def new_product(cls, my_dict):
        """Добавление экземпляра из словаря"""
        name = my_dict["name"]
        description = my_dict["description"]
        price = my_dict["price"]
        quantity = my_dict["quantity"]
        instance = cls(name, description, price, quantity)
        return instance

    @property
    def price(self):
        """Геттер для использования цены продукта"""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для исключения перезаписи цены ниже нуля"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self):
        """Строковое значение класса"""
        return f"{self.name}, {self.__price}. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение экземпляров одного класса"""
        if isinstance(other, self.__class__):
            return self.quantity * self.__price + other.quantity * other.__price
        raise TypeError("Можно складывать объекты только одного класса")


product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
print(str(product1))
