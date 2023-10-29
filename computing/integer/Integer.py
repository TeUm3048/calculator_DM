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

    def __str__(self):
        return str(self.sign)[:1] + str(self.number)

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

    def deternitane_sign(self) -> Literal[0, 1, 2]:
        if self.sign == 1:
            return 2
        if self.sign == -1:
            return 1
        return 0

    def multiply_by_negative_one(self) -> None:
        self.sign = self.sign * (-1)


if __name__ == '__main__':
    s = Integer("6")
    print(s, "sdfs")
