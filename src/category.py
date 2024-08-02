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


if __name__ == '__main__':
    smart_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    smart_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    smartphones_category = Category("Смартфоны", "Техника", [smart_1, smart_2])

    fruit_1 = Product("Яблоко", "Зеленое", 25.0, 15)
    fruits_category = Category("Фрукты", "Полезности", [fruit_1])

    print(str(smartphones_category.products))
    print(str(fruits_category.products))