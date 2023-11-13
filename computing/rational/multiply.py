# Модуль: MUL_QQ_Q
# Автор: Комосский_Егор_2381

from computing.rational.Rational import Rational


def multiply(self: Rational, other: Rational) -> Rational:
    num1 = self.copy()
    num2 = other.copy()
    return Rational([num1.numerator.multiply(num2.numerator),
                     num1.denominator.multiply(num2.denominator)]).simplify()
