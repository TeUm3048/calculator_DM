from __future__ import annotations
from typing import Literal

from computing.natural.Natural import Natural

Sign = Literal[-1, 1, 0]


class Integer:
    number: Natural
    sign: Sign

    def __init__(self, value: str | Natural) -> None:
        """ Make an Integer. """
        # Если тип значения Natural, то создаётся положительный Integer с абсолютным значением = value
        if isinstance(value, Natural):
            self.number = value
            self.sign = 1
            return
        # Если значение отрицательное, то создаётся отрицательный Integer с абсолютным значением = value
        if value[0] == '-':
            self.number = Natural(value[1:])
            self.sign = -1
        # В остальныйх случаях создаётся положительный Integer с абсолютным значением = value
        else:
            self.number = Natural(value)
            self.sign = 1
        if self.number == Natural('0'):
            self.sign = 0

    def __len__(self):
        """ Return len of self.number. """
        return len(self.number)

    def __int__(self):
        """ Cast self to int. """
        return int(self.number) * self.sign

    def copy(self):
        """ Return copy of self. """
        return Integer(str(self))

    def __str__(self):
        """ Return str(self). """
        # Если число негативное, то в начало строкового представления числа дописывается минус
        return ('-' * (self.sign < 0)) + str(self.number)

    def __repr__(self):
        return f"Integer({self})"

    def __lt__(self, other: Integer) -> bool:
        """ Return self is not equal to the other. """
        if self.sign < other.sign:
            return True
        if self.sign > other.sign:
            return False
        if self.sign == 1:
            return self.number < other.number
        if self.sign == -1:
            return self.number > other.number
        return False

    def __eq__(self, other: Integer) -> bool:
        """ Return self is not equal to the other. """
        return self.sign == other.sign and self.number == other.number

    def __le__(self, other: Integer) -> bool:
        """ Return self is not equal to the other. """
        return (self < other) or (self == other)

    def __ne__(self, other: Integer) -> bool:
        """ Return self is not equal to the other. """
        return not (self == other)

    def __gt__(self, other: Integer) -> bool:
        """ Return self is greater than the other. """
        return not (self <= other)

    def __ge__(self, other: Integer) -> bool:
        """ Return self as much as the other. """
        return not (self < other)

    def absolute(self) -> Natural:
        """ Return self-number. """
        return self.number

    def determinate_sign(self) -> Literal[0, 1, 2]:
        """ Return 2 if number is positive, 1 if number is negative, else 0. """
        if self.sign == 1:
            return 2
        if self.sign == -1:
            return 1
        return 0

    @staticmethod
    def from_natural(natural: Natural):
        """ Return Integer made from Rational. """
        return Integer(natural)

    def to_natural(integer: Integer):
        """ Return Natural made from Integer if Integer is not negative. """
        if integer < 0:
            raise ValueError("отрицательное")
        return Natural(integer.number)

    def multiply_by_negative_one(self) -> Integer:
        num = self.copy()
        num.sign = num.sign * (-1)
        return num

    def mod(self, other: Integer) -> Integer:
        from .mod import mod
        return mod(self, other)

    def __add__(self, other: Integer) -> Integer:
        return self.add(other)

    def __sub__(self, other: Integer) -> Integer:
        return self.subtract(other)

    def add(self, other: Integer) -> Integer:
        from .add import add
        return add(self, other)

    def subtract(self, other: Integer) -> Integer:
        from .subtract import subtract
        return subtract(self, other)

    def multiply(self, other: Integer) -> Integer:
        from .multiply import multiply
        return multiply(self, other)

    def div(self, other: Integer) -> Integer:
        from .div import div
        return div(self, other)


if __name__ == '__main__':
    s = Natural('26')
    k = Integer.from_natural(s)
    print(k.sign)
