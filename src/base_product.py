from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, my_dict):
        """Добавление экземпляра из словаря"""

    @property
    @abstractmethod
    def price(self):
        """Геттер для использования цены продукта"""
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        """Сеттер для исключения перезаписи цены ниже нуля"""
        pass
