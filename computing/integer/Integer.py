from __future__ import annotations
from typing import Literal

from computing.natural.Natural import Natural

Sign = Literal[-1, 1, 0]


class Integer:
    number: Natural
    sign: Sign

    def __init__(self, value: str | Natural) -> None:
        if isinstance(value, Natural):
            self.number = value
            self.sign = 1
            return
        if value[0] == '0':
            self.number = Natural('0')
            self.sign = 0
        elif value[0] == '-':
            self.number = Natural(value[1:])
            self.sign = -1
        else:
            self.number = Natural(value)
            self.sign = 1

    def __len__(self):
        return len(self.number)

    def __int__(self):
        return int(self.number) * self.sign

    def copy(self):
        return Integer(str(self))

    def __str__(self):
        return ('-' * (self.sign < 0)) + str(self.number)

    def __repr__(self):
        return f"Integer({self})"

    def __lt__(self, other: Integer) -> bool:
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
        return self.sign == other.sign and self.number == other.number

    def __le__(self, other: Integer) -> bool:
        return (self < other) or (self == other)

    def __ne__(self, other: Integer) -> bool:
        return not (self == other)

    def __gt__(self, other: Integer) -> bool:
        return not (self <= other)

    def __ge__(self, other: Integer) -> bool:
        return not (self < other)

    def absolute(self) -> Natural:
        return self.number

    def determinate_sign(self) -> Literal[0, 1, 2]:
        if self.sign == 1:
            return 2
        if self.sign == -1:
            return 1
        return 0

    @staticmethod
    def from_natural(natural: Natural):
        return Integer(natural)

    def to_natural(integer: Integer):
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
