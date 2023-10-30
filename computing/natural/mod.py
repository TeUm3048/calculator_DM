# Модуль: MOD_NN_N
# Автор: Кузнецов_Илья_2381

from .Natural import Natural
# from div import div
# from subtract_product_from_natural import subtract_product_from_natural


def mod(num1: Natural, num2: Natural) -> Natural:
    if not num2.is_not_zero():
        raise ZeroDivisionError
    return num1.subtract(num1.div(num2).multiply(num2))
