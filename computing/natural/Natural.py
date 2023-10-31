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
        """ Return len(self). """
        return len(self.data)

    def __int__(self):
        """ Return int(self). """
        return int(''.join(list(map(str, self.data)))[::-1])

    def __lt__(self, other: Natural) -> bool:
        """ Return self>value. """
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
        """ Return self==value. """
        if self is other:
            return True
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self.data[i] != other.data[i]:
                return False
        return True

    def __le__(self, other: Natural) -> bool:
        """ Return self<=value. """
        return (self < other) or (self == other)

    def __ne__(self, other: Natural) -> bool:
        """ Return self!=value. """
        return not (self == other)

    def __gt__(self, other: Natural) -> bool:
        """ Return self>value. """
        return not (self <= other)

    def __ge__(self, other: Natural) -> bool:
        """ Return self>value. """
        return not (self < other)

    def copy(self):
        """ Return a copy of B. """
        return Natural(str(self))

    def comparator(self, other: Natural) -> Literal[-1, 0, 1]:
        """
        Comparison of natural numbers

        Return 1 if self > other,
            0 if self == other,
            and -1 self < other.
        """
        if self < other:
            return -1
        if self > other:
            return 1
        return 0

    def compare(self, other: Natural) -> Literal[0, 1, 2]:
        """
        Comparison of natural numbers

        Return 2 if self > other,
            0 if self == other,
            and 1 self < other.
        """
        if self > other:
            return 2
        if self < other:
            return 1
        return 0

    def __bool__(self):
        """True if self != 0. Called for bool(self)."""
        return self.is_not_zero()

    def is_not_zero(self) -> bool:
        """ Return True if self != 0, False otherwise. """
        return not (len(self) == 1 and self.data[0] == 0)

    def increment(self) -> None:
        """ Add 1 to self """
        from .increment import increment
        increment(self)

    def add(self, other: Natural) -> Natural:
        """ Return self+value. """
        return Natural(str(int(self) + int(other)))

    def __add__(self, other: Natural):
        """ Return self+value. """
        return self.add(other)

    def __sub__(self, other):
        """ Return self-value. """
        return self.subtract(other)

    def subtract(self, other: Natural) -> Natural:
        """ Return self-value. """
        from .subtract import subtract
        return subtract(self, other)

    def multiply_by_digit(self, other: Digit) -> Natural:
        """ Return self*Digit. """
        from .multiply_by_digit import multiply_by_digit
        return multiply_by_digit(self, other)

    def multiply_by_power_of_10(self, k: Natural) -> Natural:
        """ Return self * 10^k. """
        from .multiply_by_power_of_10 import multiply_by_power_of_10
        return multiply_by_power_of_10(self, k)

    def multiply(self, other: Natural) -> Natural:
        """ Return self*other. """
        from .multiply import multiply
        return multiply(self, other)

    def __mul__(self, other: Natural | Digit) -> Natural:
        """ Return self*other. """
        if isinstance(other, Natural):
            return self.multiply(other)
        if other in Digit:
            return self.multiply_by_digit(other)
        raise ValueError("Argument must be equal Natural or Digit")

    def subtract_product_from_natural(self, other: Natural, k: Digit) -> Natural:
        """ Return self - k * other. """
        from .subtract_product_from_natural import subtract_product_from_natural
        return subtract_product_from_natural(self, other, k)
        pass

    def get_digit_of_division_with_power(self, other: Natural) -> Natural:
        """ Return first digit of division seld by other with ends zeros

        Example:
            a = Natural("115")
            b = Natural("2")
            res = a.get_digit_of_division_with_power(b)
            res
            ---------
            Natural(50)
        """
        from .get_digit_of_division_with_power import get_digit_of_division_with_power
        return get_digit_of_division_with_power(self, other)

    def div(self, other: Natural) -> Natural:
        """ Return self//other. """
        from .div import div
        return div(self, other)

    def __floordiv__(self, other: Natural):
        """ Return self//other. """
        return self.div(other)

    def mod(self, other: Natural) -> Natural:
        """ Return self%other. """
        from .mod import mod
        return mod(self, other)

    def __mod__(self, other: Natural) -> Natural:
        """ Return self%other. """
        return self.mod(other)

    def gcd(self, other: Natural) -> Natural:
        """ Greatest Common Divisor. """
        from .gcd import gcd
        return gcd(self, other)

    def lcm(self, other: Natural) -> Natural:
        """ Least Common Multiple. """
        from .lcm import lcm
        return lcm(self, other)

    def __str__(self):
        """ Return str(self). """
        return "".join(str(digit) for digit in self.data[::-1])

    def __repr__(self):
        """ Return repr(self). """
        return f"Natural({self})"
