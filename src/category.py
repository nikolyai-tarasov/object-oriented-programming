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

    @classmethod
    def add_product(cls, products):
        cls.__products = products
        return products

    @property
    def products(self):
        return self.__products

    @property
    def descriptions(self):
        return f'{self.name}.Остаток: {self.count_product}шт.'
