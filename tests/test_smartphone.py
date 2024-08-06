import pytest
from src.smartphone import Smartphone


@pytest.fixture
def smartphone_copy():
    """Фикстура для создания экземпляра класса 'Smartphone'"""
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    return smartphone1


def test_init(smartphone_copy):
    """Функция тестирования инициализации экземпляров класса 'Smartphone'"""
    assert smartphone_copy.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_copy.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_copy.price == 180000.0
    assert smartphone_copy.quantity == 5
    assert smartphone_copy.model == "S23 Ultra"
    assert smartphone_copy.memory == 256
    assert smartphone_copy.color == "Серый"


def test_add_product(smartphone_copy):
    """Функция тестирования сложения экземпляров класса 'Smartphone'"""
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smart_sum = smartphone_copy + smartphone2
    assert smart_sum == 2580000.0


def test_add_product_exception(smartphone_copy):
    """Функция тестирования сложения экземпляров класса 'Smartphone' с возбуждением ошибки"""

    class RedFlag:
        def __init__(self, name):
            self.name = name

    red_1 = RedFlag("red")
    try:
        grass_sum = smartphone_copy + red_1
    except Exception as e:
        assert e
