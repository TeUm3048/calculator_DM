from __future__ import annotations
from computing.natural.Natural import Natural
from computing.integer.Integer import Integer
from computing.rational.Rational import Rational
from numpy.polynomial import Polynomial as numpy_polynom
from fractions import Fraction
import warnings

FLOAT_EQUAL_THRESHOLD = 0.000_000_001

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
            converted_self = self.to_numpy()
            #if converted_self.degree() != other.degree():
            #    return False
            pos = lambda x: x if x > 0 else 0
            coef1 = list(converted_self.coef) + [0.0] * (pos(other.degree() - converted_self.degree()))
            coef2 = list(other.coef) + [0.0] * (pos(converted_self.degree() - other.degree()))
            
            for c1, c2 in zip(coef1, coef2):
                if abs(c1 - c2) > FLOAT_EQUAL_THRESHOLD:
                    return False
            return True

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

    def gcd(self, other: Polynom) -> Polynom:
        from .gcd import gcd
        return gcd(self, other)

    def __getitem__(self, index: int | slice) -> Rational:
        return self.data[index]

    def __setitem__(self, index: int, value: Rational) -> None:
        self.data[index] = value

    def degree(self) -> int:
        return self.get_degree()

    def is_null(self) -> bool:
        return self == Polynom([Rational("0")])

    def to_numpy(self) -> numpy_polynom:
        return numpy_polynom(list(map(float, self.data)))

    @staticmethod
    def from_numpy(polynomial: numpy_polynom):
        fraction_data = map(Fraction.from_float, polynomial.coef)
        from_fraction_to_rational = lambda x: Rational(f"{x.numerator}/{x.denominator}")
        rational_data = list(map(from_fraction_to_rational, fraction_data))
        return Polynom(rational_data)
    
    def copy(self) -> Polynom:
        return Polynom([coefficient.copy() for coefficient in self.data])

    def multiply(self, other: Polynom):
        ### ЗАГЛУШКА ###
        warnings.warn('Вместо multiply используется заглушка')
        return Polynom.from_numpy(self.to_numpy() * other.to_numpy())

 
    def divide(self, other: Polynom) -> Polynom:
        from .divide import divide
        return self.divide(other)

    def eliminating_duplicate_roots(self):
        """
        Reducing a polynomial:
         Eliminating multiple roots into prime roots
         For example,
         f(x) = (x-1) * (x-2)^2 * (x-3)^3,
         Then result equals (x-1) * (x-2) * (x-3)
        """
        f_der = self.derive()
        d = self.gcd(f_der)
        return self.divide(d)

    def multiply_by_monomial(self: Polynom, k: int | Natural) -> Polynom:
        from .multiply_by_monomial import multiply_by_monomial
        return multiply_by_monomial(self, k)

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

    def derive(self: Polynom) -> Polynom:
        from .derive import derive
        return derive(self)

    def factor_polynomial_coefficients(self: Polynom) -> Polynom:
        from .factor_polynomial_coefficients import factor_polynomial_coefficients
        return factor_polynomial_coefficients(self)

    def mod(self: Polynom, other: Polynom) -> Polynom:
        from .mod import mod
        return mod(self, other)

    def multiply_by_scalar(self: Polynom, scalar: Rational) -> Polynom:
        from .multiply_by_scalar import multiply_by_scalar
        return multiply_by_scalar(self, scalar)
