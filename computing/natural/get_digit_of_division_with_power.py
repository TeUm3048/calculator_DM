# Модуль: DIV_NN_Dk
# Автор: Мавликаев_Иван_2381

from .Natural import Natural
from .Natural import Digit

def get_digit_of_division_with_power(num1: Natural, num2: Natural) -> Digit:
    divider = 0
    dividend = 0
    if len(num1) > len(num2) or len(num1) == len(num2) and num1>=num2:
        dividend = num1 
        divider = num2
    else:
        dividend = num2
        divider = num1
    if dividend == [0]:
        return 0
    if divider == [0]:
        return ZeroDivisionError
    if dividend[:len(divider)] > divider:
        dividend = dividend[:len(divider)]
    else:
        dividend = dividend[:len(divider) + 1]
    count = Natural("0")
    while (len(dividend) > len(divider) and (dividend[1:]>=divider or dividend[0] > 0) or
        len(dividend) == len(divider) and dividend>=divider):
        for i in range (1, len(divider) + 1):
            dividend[-i] -= divider[-i]
            if dividend[-i + 1] < 0:
                dividend[-i + 1] += 10
                dividend[-i] -= 1
            if dividend[-i] < 0 and i == len(divider) and dividend[0] > 0:
                dividend[-i] += 10
                dividend[-i - 1] -= 1
        count += Natural("1")
    return count.multiply_by_power_of_10(max(len(num1, num2)) - len(dividend))
    # return multiply_by_power_of_10([count], max(len(num1, num2)) - len(dividend))