# Модуль: DIV_ZZ_Z
# Автор: Ваньков_Ярослав_2382

from computing.rational.Rational import Rational
from computing.integer.Integer import Integer


def divide(self: Rational, other: Rational):
    num1 = self.copy()
    num2 = other.copy()
    num2.numerator, num2.denominator = Integer.from_natural(
        num2.denominator).multiply(Integer(str(num2.numerator.sign))), num2.numerator.number
    return num1.multiply(num2).simplify()