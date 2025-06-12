import math 
import pytest
def sum_of(x):
    return x+5
def test_sum():
    assert sum_of(2) ==7


def test_zreodivision():
    with pytest.raises(ZeroDivisionError):
        print("about to divide by zero")
        1/0
    print("ZerDivisionError successfully caught")    


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def stsquare():
    num = 7
    assert 7*7 == 20

def testequality():
    assert 10 == 11

def power():
    assert pow(2,3) == 8   
    
