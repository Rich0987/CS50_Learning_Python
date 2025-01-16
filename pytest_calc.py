import pytest
from unit_test_calc import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
                                #we can split up the test too
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

# pytest pytest_calc.py

# when + not *
#FAILED pytest_calc.py::test_positive - assert 6 == 9
#FAILED pytest_calc.py::test_negative - assert -4 == 4
#test_zero passed

def test_str():
    with pytest.raises(TypeError):
        square("cat")