from __future__ import annotations
from typing import Literal
from computing.natural.Natural import Natural
from computing.integer.Integer import Integer


class Rational:
    numerator: Integer
    denominator: Natural

    def __init__(self, value: str | list[Integer, Natural]) -> None:
        if isinstance(value, str):
            value = value.split('/')
            if len(value) == 1:
                self.numerator = Integer(value[0])
                self.denominator = Natural('1')
            else:
                self.numerator = Integer(value[0])
                self.denominator = Natural(value[1])
            if self.denominator == Natural('0'):
                raise ZeroDivisionError
        else:
            self.numerator = value[0]
            self.denominator = value[1]
            if self.denominator == Natural('0'):
                raise ZeroDivisionError

    # def __int__(self):
    #     return int(self.number) * self.sign
    def simplify(self: Rational):
        gcd = self.numerator.number.gcd(self.denominator)
        return Rational([self.numerator.div(Integer.from_natural(gcd)),
                         self.denominator.div(gcd)])

    def copy(self):
        return Rational(str(self))

    def __str__(self: Rational):
        return (str(self.numerator) + ('/' + str(self.denominator))
                * (self.denominator != Natural('1')))

    def __repr__(self):
        return f"Rational({self})"

    def is_integer(self: Rational):
        return self.denominator == Natural('1')

    @staticmethod
    def from_integer(int: Integer):
        return Rational(int, Natural('1'))

    @staticmethod
    def to_integer(rat: Rational):
        num1 = rat.copy().simplify()
        if num1.denominator == Natural('1'):
            return num1.numerator
        return rat ## под вопросом

    def __add__(self, other: Rational) -> Rational:
        return self.add(other)

    def __sub__(self, other: Rational) -> Rational:
        return self.subtract(other)

    def add(self: Rational, other: Rational) -> Rational:
        from .add import add
        return add(self, other)

    def subtract(self: Rational, other: Rational) -> Rational:
        from .subtract import subtract
        return subtract(self, other)

    def multiply(self: Rational, other: Rational) -> Rational:
        from .multiply import multiply
        return multiply(self, other)

    def divide(self: Rational, other: Rational) -> Rational:
        from .divide import divide
        return divide(self, other)
    # def __lt__(self, other: Integer) -> bool:
    #     if self.sign < other.sign:
    #         return True
    #     if self.sign > other.sign:
    #         return False
    #     if self.sign == 1:
    #         return self.number < other.number
    #     if self.sign == -1:
    #         return self.number > other.number
    #     return False

    # def __eq__(self, other: Integer) -> bool:
    #     return self.sign == other.sign and self.number == other.number

    # def __le__(self, other: Integer) -> bool:
    #     return (self < other) or (self == other)

    # def __ne__(self, other: Integer) -> bool:
    #     return not (self == other)

    # def __gt__(self, other: Integer) -> bool:
    #     return not (self <= other)

    # def __ge__(self, other: Integer) -> bool:
    #     return not (self < other)


if __name__ == '__main__':
    s = Rational('7/2')
    k = Rational('9/3')
    print(s.devide(k))
