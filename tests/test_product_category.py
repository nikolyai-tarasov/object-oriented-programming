import pytest
from src.product_category import Product, Category


@pytest.fixture
def product_appal():
    return Product(name="appal", description="fruit", price=150, quantity=124)


def test_product(product_appal):
    assert product_appal.name == "appal"
    assert product_appal.description == "fruit"
    assert product_appal.price == 150
    assert product_appal.quantity == 124


@pytest.fixture
def category_fruit():
    return Category(name="fruit", description="tropical", products=["banana", "papaya", "coconut"])


def test_category(category_fruit):
    assert category_fruit.name == "fruit"
    assert category_fruit.description == "tropical"
    assert category_fruit.products == ["banana", "papaya", "coconut"]
    assert category_fruit.count_category == 1
    assert category_fruit.count_product == 3
