# Модуль: DIV_ZZ_Z
# Автор: Мавликаев_Иван_2381

# Деление нацело целых чисел
from .Integer import Integer, Natural


def div(num1: Integer, num2: Integer) -> Integer:
    # Если второе число 0, выкидывается ошибка
    if not num2.number.is_not_zero():
        raise ZeroDivisionError
    # Если перввое число 0 - возввращается 0
    if not num1.number.is_not_zero():
        return Integer("0")
    # Вычисляется модуль результата с помощью метода div для натуральных чисел (класс Natural)
    res = Integer(num1.number.div(num2.number))
    # У результата вычисляется знак в зависимости от знаков делителя и делимого 
    if num2.sign > 0 > num1.sign:
        #Для того, чтобы mod был положительным, в случае, когда первое число отрицательное а втроре полжительное, к результату добавляется единица
        res.sign = -1
        if num1.number != num2.number.multiply(res.number):
            res.number = res.number.add(Natural("1"))
    #Для того, чтобы mod был положительным, в случае, когда оба исхходных числа отрицательные, к результату добавляется единица
    if num1.sign < 0 and num2.sign < 0:
        if num1.number != num2.number.multiply(res.number):
            res.number = res.number.add(Natural("1"))
    if num1.sign > 0 > num2.sign:
        res.sign = -1
    return res
