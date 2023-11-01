# Модуль: SUB_QQ_Q
# Автор: Комосский_Егор_2381

from computing.rational.Rational import Rational


def subtract(self: Rational, other: Rational) -> Rational:
    num1 = self.copy()
    num2 = other.copy()
    num2.numerator = num2.numerator.multiply_by_negative_one()
    return num1.add(num2)
