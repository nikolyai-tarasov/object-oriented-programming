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
    x = {'name': 'appal',
         'description': 'fruit',
         'price': 150,
         'quantity': 124}
    prod_1 = Product.new_product(x)
    assert prod_1.name == 'appal'
    assert prod_1.price == 150
    assert prod_1.quantity == 124
    assert prod_1.description == 'fruit'
