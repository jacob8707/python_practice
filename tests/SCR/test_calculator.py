from app.SCR.calculator import Calculator
cal=Calculator()
def test_sum():
    assert cal.sum(1,1)==2
    assert cal.sum(2,1)==3


def test_subtract():
    assert cal.subtract(3,1)==2

def test_divide():
    assert cal.divide(10,0)=='Error! The dividing number can NOT be zero'


def test_fdivide():
    assert cal.fdivide(10,6)==1


def test_remainder():
    assert cal.remainder(3,2)==1



