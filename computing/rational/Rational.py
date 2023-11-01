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
                self.numerator = Integer(value)
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

    def add(self: Rational, other: Rational):
        num1 = self.copy()
        num2 = other.copy()
        lcm = num1.denominator.lcm(num2.denominator)
        new_numer = (num1.numerator.multiply(Integer.from_natural(
            lcm.div(num1.denominator)))).add(
                num2.numerator.multiply(
                    Integer.from_natural(lcm.div(num2.denominator))))
        return Rational([new_numer, lcm]).simplify()

    def subtract(self: Rational, other: Rational):
        num1 = self.copy()
        num2 = other.copy()
        num2.numerator = num2.numerator.multiply_by_negative_one()
        return num1.add(num2)

    def multiply(self: Rational, other: Rational):
        num1 = self.copy()
        num2 = other.copy()
        return Rational([num1.numerator.multiply(num2.numerator),
                         num1.denominator.multiply(num2.denominator)])

    def devide(self: Rational, other: Rational):
        num1 = self.copy()
        num2 = other.copy()
        num2.numerator, num2.denominator = Integer.from_natural(
            num2.denominator).multiply(Integer(str(num2.numerator.sign))), num2.numerator.number
        return num1.multiply(num2)
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
