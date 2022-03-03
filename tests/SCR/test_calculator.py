from app.SCR.calculator import Calculator
cal=Calculator()
def test_sum():
    assert cal.sum(1,1)==2
    assert cal.sum(2,1)==3

