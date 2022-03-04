from app.SCR.calculator import Calculator
cal=Calculator()
def test_sum():
    assert cal.sum(1,1)==2
    assert cal.sum(2,1)==3

def test_divide():
    assert cal.divide(10,0)=='Error! The dividing number can NOT be zero'


