# Модуль: ADD_PP_P
# Автор: Кривов_Савелий_2381

from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational


def add(self: Polynom, other: Polynom) -> Polynom:
    num1 = self
    num2 = other

    res = Polynom([])
    while len(num1.data) < len(num2.data):
        num1.data.append(Rational("0"))
    while len(num2.data) < len(num1.data):
        num2.data.append(Rational("0"))

    for i in range(len(num1.data)):
        res.data.append(num1.data[i].add(num2.data[i]))
    return res
