from __future__ import annotations
from typing import Literal
import math

Digit = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


class Natural:
    data: list[Digit]

    def __init__(self, value: str) -> None:
        self.data = []
        for digit in value:
            self.data = [int(digit)] + self.data

    def __len__(self):
        return len(self.data)

    def __int__(self):
        return int(''.join(list(map(str, self.data)))[::-1])

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

    def __mod__(self, other: Natural) -> Natural:
        return Natural(str(int(self) % int(other)))
        # РАСКОММЕНТИТЬ ЕСЛИ ПОНАДОБИТСЯ А НИЖЕ НЕ НАПИСАН КОД
        pass

    def copy(self):
        return Natural(str(self))

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

    def increment(self) -> None:
        from .increment import increment
        increment(self)
        # self.data = Natural(str(int(self)+1)).data

        # РАСКОММЕНТИТЬ ЕСЛИ ПОНАДОБИТСЯ А НИЖЕ НЕ НАПИСАН КОД

    def add(self, other: Natural) -> Natural:
        return Natural(str(int(self) + int(other)))
        # РАСКОММЕНТИТЬ ЕСЛИ ПОНАДОБИТСЯ А НИЖЕ НЕ НАПИСАН КОД
        # pass

    def __add__(self, other: Natural):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def subtract(self, other: Natural) -> Natural:
        from .subtract import subtract
        return subtract(self, other)
        # return Natural(str(int(self)-int(other)))
        # РАСКОММЕНТИТЬ ЕСЛИ ПОНАДОБИТСЯ А НИЖЕ НЕ НАПИСАН КОД
        # НЕ ВЫЧИТАТЬ ИЗ МЕНЬШЕГО БОЛЬШЕЕ
        # pass

    def multiply_by_digit(self, other: Natural) -> Natural:
        # return Natural(str(int(self)*other))
        # РАСКОММЕНТИТЬ ЕСЛИ ПОНАДОБИТСЯ А НИЖЕ НЕ НАПИСАН КОД
        from .multiply_by_digit import multiply_by_digit
        return multiply_by_digit(self, other)

    def multiply_by_power_of_10(self, k: Natural) -> Natural:
        from .multiply_by_power_of_10 import multiply_by_power_of_10
        return multiply_by_power_of_10(self, k)

        # return Natural(str(int(self) * (10 ** int(k))))  # заглушка написан для k : int
        # РАСКОММЕНТИТЬ ЕСЛИ ПОНАДОБИТСЯ А НИЖЕ НЕ НАПИСАН КОД
        # pass

    def multiply(self, other: Natural) -> Natural:
        # return Natural(str(int(self)*int(other)))
        # РАСКОММЕНТИТЬ ЕСЛИ ПОНАДОБИТСЯ А НИЖЕ НЕ НАПИСАН КОД
        from .multiply import multiply
        return multiply(self, other)

    def __mul__(self, other: Natural | Digit) -> Natural:
        if isinstance(other, Natural):
            return self.multiply(other)
        if other in Digit:
            return self.multiply_by_digit(other)
        raise ValueError("Argument must be equal Natural or Digit")

    def subtract_product_from_natural(self, other: Natural, k: int) -> Natural:
        # return Natural(str(int(self) - k * int(other)))
        # РАСКОММЕНТИТЬ ЕСЛИ ПОНАДОБИТСЯ А НИЖЕ НЕ НАПИСАН КОД
        from .subtract_product_from_natural import subtract_product_from_natural
        return subtract_product_from_natural(self, other, k)
        pass

    def get_digit_of_division_with_power(self, other: Natural) -> Natural:
        # я сам не понял че надо так шо надо будет подумать
        res = str(int(self) // int(other))
        a000000 = res[0] + "0" * (len(res) - 1)
        return Natural(a000000)
        # РАСКОММЕНТИТЬ ЕСЛИ ПОНАДОБИТСЯ А НИЖЕ НЕ НАПИСАН КОД
        pass

    def div(self, other: Natural) -> Natural:
        from .div import div
        return div(self, other)

    def __floordiv__(self, other: Natural):
        return self.div(other)

    def mod(self, other: Natural) -> Natural:
        from .mod import mod
        return mod(self, other)

    def gcd(self, other: Natural) -> Natural:
        from .gcd import gcd
        return gcd(self, other)
        # return Natural(str(math.gcd(int(self), int(other))))
        # РАСКОММЕНТИТЬ ЕСЛИ ПОНАДОБИТСЯ А НИЖЕ НЕ НАПИСАН КОД
        # pass

    def lcm(self, other: Natural) -> Natural:
        from .lcm import lcm
        return lcm(self, other)
        # РАСКОММЕНТИТЬ ЕСЛИ ПОНАДОБИТСЯ А НИЖЕ НЕ НАПИСАН КОД
        pass

    def __str__(self):
        return "".join(str(digit) for digit in self.data[::-1])

    def __repr__(self):
        return f"Natural({self})"
