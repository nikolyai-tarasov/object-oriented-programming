import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def category_phones():
    """Фикстура для примеров тестирования"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    category1.add_product(product4)
    return category1


def test_category(category_phones):
    """Функция тестирования конструктора класса"""
    assert category_phones.name == "Смартфоны"
    assert category_phones.count_category == 1
    assert category_phones.count_product == 4


def test_str(category_phones):
    """Функция тестирования стокового значения класса"""
    assert str(category_phones) == f"{category_phones.name}, количество продуктов: 34 шт."


def test_add_product(category_phones):
    """Функция тестирования добавления продукта к уже имеющемуся списку"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    assert category_phones.add_product(product1) == None
    assert category_phones.add_product(smartphone1) == None


def test_add_product_exception(category_phones):
    """Функция тестирования вызова исключения"""
    class RedFlag:
        def __init__(self, name):
            self.name = name

    red_1 = RedFlag("red")
    try:
        category_phones.add_product(red_1)
    except Exception as e:
        assert e
