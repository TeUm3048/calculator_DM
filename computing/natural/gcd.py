# Модуль: GCF_NN_N
# Автор: Ильясов_Марк_2381

from .Natural import Natural
from mod import mod
from compare import compare
from subtract_product_from_natural import subtract_product_from_natural


def gcd(num1: Natural, num2: Natural) -> Natural:
    a = num1.copy()
    b = num2.copy()

    if not (a.is_not_zero() and b.is_not_zero()):
        # todo: продумать какую ошибку кидать
        raise ZeroDivisionError

    while a.is_not_zero() and b.is_not_zero():
        a %= b
        a, b = b, a
    return max(a, b)
