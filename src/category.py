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

    @property
    def products(self):
        product = ""
        for i in self.__products:
            product += f"{i.name}, {round(i.price)} руб. Остаток: {i.quantity}.\n"
        return product

    def add_product(self, product):
        self.__products.append(product)
        Category.count_product += 1

    def __str__(self):
        return f"{self.name}, количество продуктов: {Product.counter_of_all_products} шт."
