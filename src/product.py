from src.base_product import BaseProduct
from src.mixin_log import MixinLog


class Product(MixinLog, BaseProduct):
    """Класс 'Product' создает экземпляры продуктов"""
    name: str
    description: str
    price: int
    quantity: int
    counter_of_all_products = 0
    avg_price = 0

    def __init__(self, name, description, price, quantity):
        """Конструктор класса"""
        super().__init__(name, description, price, quantity)
        Product.counter_of_all_products += quantity
        super().__repr__()
        Product.avg_price += self.price
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

    @classmethod
    def new_product(cls, my_dict):
        """Добавление экземпляра из словаря"""
        name = my_dict["name"]
        description = my_dict["description"]
        price = my_dict["price"]
        quantity = my_dict["quantity"]
        instance = cls(name, description, price, quantity)
        return instance

    def __str__(self):
        """Строковое значение класса"""
        return f"{self.name}, {self.price}. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение экземпляров одного класса"""
        if isinstance(other, self.__class__):
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError("Можно складывать объекты только одного класса")
