class MixinLog:
    def __init__(self, name, description, price, quantity):
        """Конструктор класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', '{self.__price}', '{self.quantity}')"
