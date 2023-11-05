from __future__ import annotations
from computing.natural.Natural import Natural
from computing.integer.Integer import Integer
from computing.rational.Rational import Rational
from numpy.polynomial import Polynomial as numpy_polynom

class Polynom:
    data: list[Rational]

    def __init__(self, value: list[Rational]) -> None:
        if value == []:
            self.data = [Rational("0")]
            return
        self.data = value
        while len(self.data) > 1 and self.data[-1] == Rational("0"):
            self.data.pop()

    def __len__(self):
        return len(self.data)
    
    def __eq__(self, other: Polynom | numpy_polynom):
        if isinstance(other, numpy_polynom):
            return self.to_numpy() == other

        if self.degree() != other.degree():
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True
    
    def __str__(self) -> str:
        s = ", ".join(str(x) for x in self.data)
        return f"[{s}]"

    def __repr__(self) -> str:
        return f"Polynom({self})"
    
    def __getitem__(self, index: int | slice) -> Rational:
        return self.data[index]
    
    def __setitem__(self, index: int, value: Rational) -> None:
        self[index] = value

    def degree(self) -> int:
        return len(self) - 1
    
    def is_null(self) -> bool:
        return self.data == Polynom([Rational("0")])

    def to_numpy(self) -> numpy_polynom:
        return numpy_polynom(map(float, self.data))

    def copy(self) -> Polynom:
        return Polynom([coefficient.copy() for coefficient in self.data])


    def get_degree(self):
        from .get_degree import get_degree
        return get_degree(self)

    def get_leading_coefficient(self):
        from .get_leading_coefficient import get_leading_coefficient
        return get_leading_coefficient(self)

    def copy(self):
        return Polynom(list(self.data))

    def add(self: Polynom, other: Polynom) -> Polynom:
        from .add import add
        return add(self, other)

    def subtract(self: Polynom, other: Polynom) -> Polynom:
        from .subtract import subtract
        return subtract(self, other)

    def factor_polynomial_coefficients(self: Polynom) -> Polynom:
        from .factor_polynomial_coefficients import factor_polynomial_coefficients
        return factor_polynomial_coefficients(self)
  
    def mod(self: Polynom, other: Polynom) -> Polynom:
        from .mod import mod
        return mod(self, other)

    def multiply_by_scalar(self: Polynom, scalar: Rational) -> Polynom:
        from .multiply_by_scalar import multiply_by_scalar
        return multiply_by_scalar(self, scalar)
