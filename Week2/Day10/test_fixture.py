import pytest
class Cart:
    def __init__(self):
        self.items = []

    def add(self,item):
        self.items.append(item)

    def count(self):
        return len(self.items)


@pytest.fixture
def empty_cart():
    return Cart()

def test_cart_starts_empty(empty_cart):
    assert empty_cart.count()==0

def test_adding_items(empty_cart):
    empty_cart.add("apple") 
    assert empty_cart.count() ==1           
