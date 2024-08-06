from src.product import Product


class LawnGrass(Product):
    """Класс 'LawnGrass' создает экземпляры 'Газонной травы' на основе родительского 'Product'"""
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Конструктор класса"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
