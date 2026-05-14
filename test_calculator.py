import pytest
from calculator2 import square  

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_string():
    with pytest.raises(TypeError):
        square("cat")
# assert statements will raise an AssertionError if the condition is not met
# to run the tests, use the command: python -m pytest test_calculator.py