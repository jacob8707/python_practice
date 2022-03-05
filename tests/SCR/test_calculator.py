from app.SCR.calculator import Calculator
cal=Calculator()
def test_sum():
    assert cal.sum(1,1)==2
    assert cal.sum(2,1)==3


def test_subtract():
    assert cal.subtract(3,1)==2

def test_divide():
    assert cal.divide(10,0)=='Error! The dividing number can NOT be zero'
    assert cal.divide(10,2)==5

def test_fdivide():
    assert cal.fdivide(10,6)==1
    assert cal.fdivide(10,0)=='Error! The dividing number can NOT be zero'


def test_remainder():
    assert cal.remainder(3,2)==1
    assert cal.remainder(3,0)=='Error! The dividing number can NOT be zero'

def test_multiply():
    assert cal.multiply(3,6)==18




