class Product:
    """Класс 'Product' создает экземпляры продуктов"""
    name: str
    description: str
    price: int
    quantity: int
    counter_of_all_products = 0

    def __init__(self, name, description, price, quantity):
        """Конструктор класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.counter_of_all_products += quantity

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


