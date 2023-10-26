import sys
sys.path.insert(0, './')
from isLeapYear import isLeapYear

def test_leap_years():
    assert isLeapYear(2000) == True
    assert isLeapYear(2004) == True
    assert isLeapYear(2012) == True
    assert isLeapYear(2400) == True

def test_non_leap_years():
    assert isLeapYear(1700) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(1900) == False
    assert isLeapYear(2100) == False

def test_other_years():
    assert isLeapYear(2001) == False
    assert isLeapYear(2022) == False
    assert isLeapYear(2023) == False
    assert isLeapYear(2101) == False

def test_negative_years():
    assert isLeapYear(-2000) == True
    assert isLeapYear(-1700) == False
    assert isLeapYear(-2022) == False
    assert isLeapYear(-2101) == False

def test_invalid_input():
    with pytest.raises(TypeError):
        isLeapYear("invalid")
    with pytest.raises(TypeError):
        isLeapYear(3.14)
    with pytest.raises(ValueError):
        isLeapYear(-1)

test_isLeapYear()

