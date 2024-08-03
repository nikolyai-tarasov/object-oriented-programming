import pytest

from src.product import Product


@pytest.fixture
def product_appal():
    """Фикстура экземпляра класса"""
    return Product(name="appal", description="fruit", price=150, quantity=124)


def test_product(product_appal):
    """Функция тестирования конструктора класса"""
    assert product_appal.name == "appal"
    assert product_appal.description == "fruit"
    assert product_appal.price == 150
    assert product_appal.quantity == 124


def test_latest_add_prod():
    """Функция тестирования добавления экземпляра из словаря"""
    x = {"name": "appal", "description": "fruit", "price": 150, "quantity": 124}
    prod_1 = Product.new_product(x)
    assert prod_1.name == "appal"
    assert prod_1.price == 150
    assert prod_1.quantity == 124
    assert prod_1.description == "fruit"


def test_str():
    """Функция тестирования строкового значения функции"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert str(product1) == f"{product1.name}, {product1.price}. Остаток: {product1.quantity} шт."


def test_add():
    """Функция тестирования сложения экземпляров класса 'Product'"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product1 + product2 == product1.quantity * product1.price + product2.quantity * product2.price


def test_add_product_exception():
    """Функция тестирования сложения экземпляров класса 'Product' с возбуждением ошибки"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    class RedFlag:
        def __init__(self, name):
            self.name = name

    red_1 = RedFlag("red")
    try:
        grass_sum = product1 + red_1
    except Exception as e:
        assert e
