def isLeapYear(year):
    if not isinstance(year, int):
        raise TypeError("Input must be an integer")
    if year < 0:
        raise ValueError("Year must be a non-negative integer")
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
