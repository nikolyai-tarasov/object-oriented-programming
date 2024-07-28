import pytest
from src.category import Category


@pytest.fixture
def category_fruit():
    return Category(name="fruit", description="tropical", products=["banana", "papaya", "coconut"])


def test_category(category_fruit):
    assert category_fruit.name == "fruit"
    assert category_fruit.description == "tropical"
    assert category_fruit.products == ["banana", "papaya", "coconut"]
    assert category_fruit.count_category == 1
    assert category_fruit.count_product == 3


def test_new_add(category_fruit):
    assert category_fruit.descriptions == f"{category_fruit.name}.Остаток: {category_fruit.count_product}шт."
