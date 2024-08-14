from src.product import Product


class Category:
    """Класс 'Category' создает экземпляры продуктов по категориям"""
    name: str
    description: str
    products: list
    count_category = 0
    count_product = 0
    avg_price = 0

    def __init__(self, name, description, products):
        """Конструктор класса"""
        self.name = name
        self.description = description
        self.__products = products
        Category.count_category += 1
        Category.count_product += len(products)


    def __str__(self):
        """Строковое значение класса для пользователя"""
        product = 0
        for i in self.__products:
            product += i.quantity
        return f"{self.name}, количество продуктов: {product} шт."

    def add_product(self, product):
        """Добавление продукта к уже имеющимся списку"""
        if not issubclass(product.__class__, Product):
            raise TypeError("Нельзя добавить экземпляр не класса Product")
        self.__products.append(product)
        Category.count_product += 1

    @property
    def products(self):
        """Геттер для вывода списка товаров в виде строк"""
        product = ""
        for i in self.__products:
            product += f"{str(i)}\n"
        return product

    def middle_price(self):
        try:
            return round(Product.avg_price / Category.count_product, 1)
        except ZeroDivisionError:
            return 0

