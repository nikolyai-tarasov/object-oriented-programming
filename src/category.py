from src.product import Product


class Category:
    name: str
    description: str
    products: list
    count_category = 0
    count_product = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.count_category += 1
        Category.count_product += len(products)

    def __str__(self):
        product = 0
        for i in self.__products:
            product += i.quantity
        return f"{self.name}, количество продуктов: {product} шт."

    def add_product(self, product):
        self.__products.append(product)
        Category.count_product += 1

    @property
    def products(self):
        product = ""
        for i in self.__products:
            product += f"{str(i)}\n"
        return product


