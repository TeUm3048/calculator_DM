# Модуль: DIV_NN_Dk
# Автор: Мавликаев_Иван_2381

from .Natural import Natural
from .Natural import Digit

def get_digit_of_division_with_power(num1: Natural, num2: Natural) -> Digit:
    if not num2.is_not_zero():
        raise ZeroDivisionError
        
    a = num1.copy()
    b = num2.copy()

    a.data = a.data[-len(b):]

    if a < b:
        a.data = num1.data[-len(b)+1:]
    k = Natural(str(len(num1) -  len(a)))

    count = Natural("0")

    while a >= b:
        a -= b
        count += Natural("1")
    return count.multiply_by_power_of_10(k)