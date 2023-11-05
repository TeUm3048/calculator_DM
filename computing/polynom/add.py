# Модуль: ADD_PP_P
# Автор: Кривов_Савелий_2381

from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational


def add(self: Polynom, other: Polynom) -> Polynom:
    num1 = self.copy()
    num2 = other.copy()

    min_len = min(len(num1.data), len(num2.data))
    res = [num1.data[i].add(num2.data[i]) for i in range(min_len)]

    if len(num1.data) > min_len:
        res.extend(num1.data[min_len:])
    elif len(num2.data) > min_len:
        res.extend(num2.data[min_len:])

    return Polynom(res)

