import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def category_phones():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )
    category1.add_product(product4)
    return category1


def test_category(category_phones):
    assert category_phones.name == "Смартфоны"
    assert category_phones.count_category == 1
    assert category_phones.count_product == 4
