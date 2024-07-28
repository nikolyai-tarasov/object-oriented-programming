import pytest
from src.product import Product


@pytest.fixture
def product_appal():
    return Product(name="appal", description="fruit", price=150, quantity=124)


def test_product(product_appal):
    assert product_appal.name == "appal"
    assert product_appal.description == "fruit"
    assert product_appal.price == 150
    assert product_appal.quantity == 124


def test_latest_add_prod():
    Product.new_product({'name': 'appal',
                         'description': 'fruit',
                         'price': 150,
                         'quantity': 124})
    assert Product.name == 'appal'
    assert Product.price == 150
