# DIV_PP_P
# Автор: Ильясов_Марк_2381

from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational


def divide(self: Polynom, other: Polynom) -> Polynom:
    if other.is_null():
        raise ZeroDivisionError
    if self.degree() < other.degree() or self.is_null():
        return Polynom([Rational("0")])
    
    a = self.copy()
    b = other.copy()
    result = Polynom([Rational("0")])

    while a.degree() >= b.degree() and not a.is_null():
        coefficient = a[-1] / b[-1]
        result = result.add(Polynom([coefficient]).multiply_by_monomial(a.degree() - b.degree()))
        a = a.subtract(b.multiply_by_monomial(a.degree() - b.degree()).multiply_by_scalar(coefficient))

    return result
