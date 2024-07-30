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
        name = my_dict['name']
        description = my_dict['description']
        price = my_dict['price']
        quantity = my_dict['quantity']
        instance = cls(name, description, price, quantity)
        return instance

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value


x = {'name': 'appal',
     'description': 'fruit',
     'price': 150,
     'quantity': 124}
prod_1 = Product.new_product(x)
print(prod_1.name)