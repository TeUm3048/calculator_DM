from __future__ import annotations
from typing import Literal
from computing.natural.Natural import Natural
from computing.integer.Integer import Integer


class Rational:
    numerator: Integer
    denominator: Natural

    def __init__(self, value: str) -> None:
        value = value.split('/')
        if len(value) == 1:
            self.numerator = Integer(value)
            self.denominator = Natural('1')
        else:
            self.numerator = Integer(value[0])
            self.denominator = Natural(value[1])
        if self.denominator == Natural('0'):
            raise ZeroDivisionError

    # def __int__(self):
    #     return int(self.number) * self.sign

    def copy(self):
        return Rational(str(self))

    def __str__(self: Rational):
        return (str(self.numerator) + '/' + str(self.denominator))

    def __repr__(self):
        return f"Rational({self})"

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
    s = Rational('2/6')
    print(s)
