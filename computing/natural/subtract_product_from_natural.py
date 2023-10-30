# Модуль: SUB_NDN_N
# Автор: Потапова_Дарья_2381

from .Natural import Natural, Digit


def subtract_product_from_natural(num1: Natural, num2: Natural, k: Digit) -> Natural:
    subtrahend = num2.multiply_by_digit(k)
    res = num1.subtract(subtrahend)
    return res
