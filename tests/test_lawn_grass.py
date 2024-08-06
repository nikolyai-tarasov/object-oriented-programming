import pytest
from src.lawn_grass import LawnGrass


@pytest.fixture
def lawn_grass_copy():
    """Фикстура для создания экземпляра класса 'LawnGrass'"""
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона",
                       500.0, 20, "Россия", "7 дней", "Зеленый")
    return grass1


def test_init(lawn_grass_copy):
    """Функция тестирования инициализации экземпляров класса 'LawnGrass'"""
    assert lawn_grass_copy.name == "Газонная трава"
    assert lawn_grass_copy.description == "Элитная трава для газона"
    assert lawn_grass_copy.price == 500.0
    assert lawn_grass_copy.quantity == 20
    assert lawn_grass_copy.country == "Россия"
    assert lawn_grass_copy.germination_period == "7 дней"
    assert lawn_grass_copy.color == "Зеленый"


def test_add_product(lawn_grass_copy):
    """Функция тестирования сложения экземпляров класса 'LawnGrass'"""
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    grass_sum = lawn_grass_copy + grass2
    assert grass_sum == 16750.0


def test_add_product_exception(lawn_grass_copy):
    """Функция тестирования сложения экземпляров класса 'LawnGrass' с возбуждением ошибки"""

    class RedFlag:
        def __init__(self, name):
            self.name = name

    red_1 = RedFlag("red")
    try:
        grass_sum = lawn_grass_copy + red_1
    except Exception as e:
        assert e

