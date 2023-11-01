# Модуль: ADD_QQ_Q
# Автор: Комосский_Егор_2381

from computing.rational.Rational import Rational
from computing.integer.Integer import Integer


def add(self: Rational, other: Rational) -> Rational:
    num1 = self.copy()
    num2 = other.copy()
    lcm = num1.denominator.lcm(num2.denominator)
    new_numer = (num1.numerator.multiply(Integer.from_natural(
        lcm.div(num1.denominator)))).add(
        num2.numerator.multiply(
            Integer.from_natural(lcm.div(num2.denominator))))
    return Rational([new_numer, lcm]).simplify()
