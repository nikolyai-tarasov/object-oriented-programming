class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, my_dict):
        cls.name = my_dict['name']
        cls.description = my_dict['description']
        cls.price = my_dict['price']
        cls.quantity = my_dict['quantity']

    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def get_price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")


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
    def print_desc(self):
        return f'{self.name}.Остаток: {self.count_product}шт.'


prod_1 = Product(name="Sad", description="Das", price=12, quantity=12)
prod_2 = Product(name="Sad", description="Das", price=-12, quantity=12)
print(prod_2.name)
