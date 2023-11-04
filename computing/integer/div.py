# Модуль: DIV_ZZ_Z
# Автор: Мавликаев_Иван_2381


from .Integer import Integer, Natural


def div(num1: Integer, num2: Integer) -> Integer:
    if not num2.number.is_not_zero():
        raise ZeroDivisionError
    if not num1.number.is_not_zero():
        return Integer("0")
    res = Integer(num1.number.div(num2.number))
    if num2.sign > 0 > num1.sign:
        res.sign = -1
        if num1.number != num2.number.multiply(res.number):
            res.number = res.number.add(Natural("1"))
    if num1.sign < 0 and num2.sign < 0:
        if num1.number != num2.number.multiply(res.number):
            res.number = res.number.add(Natural("1"))
    if num1.sign > 0 > num2.sign:
        res.sign = -1
    return res
