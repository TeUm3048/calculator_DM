from __future__ import annotations
from typing import Literal

Digit = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


class Natural:
    data: list[Digit]

    def __init__(self, value: str) -> None:
        self.data = []
        for digit in value:
            self.data = [int(digit)] + self.data

    def __len__(self):
        return len(self.data)

    def __lt__(self, other: Natural) -> bool:
        if len(self) > len(other):
            return False
        if len(self) < len(other):
            return True
        i = len(self) - 1
        while i >= 0 and self.data[i] == other.data[i]:
            i -= 1
        if i == -1:
            return False
        return self.data[i] < other.data[i]

    def __eq__(self, other: Natural) -> bool:
        if self is other:
            return True
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self.data[i] != other.data[i]:
                return False
        return True

    def __le__(self, other: Natural) -> bool:
        return (self < other) or (self == other)

    def __ne__(self, other: Natural) -> bool:
        return not (self == other)

    def __gt__(self, other: Natural) -> bool:
        return not (self <= other)

    def __ge__(self, other: Natural) -> bool:
        return not (self < other)

    def comparator(self, other: Natural) -> Literal[-1, 0, 1]:
        if self < other:
            return -1
        if self > other:
            return 1
        return 0

    def compare(self, other: Natural) -> Literal[0, 1, 2]:
        if self > other:
            return 2
        if self < other:
            return 1
        return 0

    def is_not_zero(self) -> bool:
        return not (len(self) == 1 and self.data[0] == 0)

    def __str__(self):
        return "".join(str(digit) for digit in self.data[::-1])
