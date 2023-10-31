# Модуль: DIV_ZZ_Z
# Автор: Мавликаев_Иван_2381

from .Integer import Integer, Natural


def div(num1: Integer, num2: Integer) -> Integer:
    if not num2.number.is_not_zero():
        raise ZeroDivisionError
    if num1.number < num2.number:
        if not num1.number.is_not_zero() or num1.sign > 0 and num2.sign < 0 or num1.sign > 0 and num2.sign > 0:
            return Integer("0")
        if num1.sign < 0 and num2.sign > 0:
            return Integer("-1")
        if num1.sign < 0 and num2.sign < 0:
            return Integer("1")
    res = Integer(num1.number.div(num2.number))
    if num1.sign == -1 and res.number.is_not_zero():
        if num1.sign != num2.sign:
            res.sign = -1
        if num1.number.mod(num2.number) != Natural("0"):
            res.number += 1
    return res