class MixinLog:
    def __init__(self, name, description, price, quantity):
        """Конструктор класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', '{self.__price}', '{self.quantity}')"
