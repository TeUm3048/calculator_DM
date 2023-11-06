# Модуль: SUB_PP_P
# Автор: Кривов_Савелий_2381

from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational


def subtract(self: Polynom, other: Polynom) -> Polynom:
    num1 = self.copy()
    num2 = other.copy()

    num2.data = [num2.data[i].multiply(Rational("-1")) for i in range(len(num2.data))]
    return num1.add(num2)

