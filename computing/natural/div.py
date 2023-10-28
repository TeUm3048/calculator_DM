# Модуль: DIV_NN_N
# Автор: Рыжиков_Иван_2381

from .Natural import Natural


# from subtract_product_from_natural import subtract_product_from_natural
# from get_digit_of_division_with_power import get_digit_of_division_with_power


def div(num1: Natural, num2: Natural) -> Natural:
    if num2 == Natural("0"):
        raise ZeroDivisionError

    a = num1.copy()
    b = num2.copy()

    res = Natural("0")

    while a >= b:
        digit_with_zeros = a.get_digit_of_division_with_power(b)
        a -= digit_with_zeros * b
        res += digit_with_zeros
    return res
