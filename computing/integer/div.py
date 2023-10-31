# Модуль: DIV_ZZ_Z
# Автор: Мавликаев_Иван_2381

from .Integer import Integer, Natural


def div(num1: Integer, num2: Integer) -> Integer:
    if not num2.number.is_not_zero():
        raise ZeroDivisionError
    res = Integer(num1.number.div(num2.number))
    if num1.sign != num2.sign and res.number.is_not_zero():
        res.sign = -1
    if not res.number.is_not_zero():
        res.sign = 0
    return res