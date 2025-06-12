import pytest
import math
@pytest.mark.square # create your own mark to test 
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

@pytest.mark.square
def testsquare():
    num = 7
    assert 7*7 == 49

@pytest.mark.others # this is also in test_compare.py file and we can execute both marks together
def test_equality():
    assert 10 == 11        