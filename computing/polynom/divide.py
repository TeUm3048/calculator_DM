# Автор: Ильясов_Марк_2381

### ВНИМАНИЕ: ЧЕРНОВИК, НЕ ПОДВЕРГАЛСЯ ТЕСТИРОВАНИЮ

import warnings
from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational

def divide(self: Polynom, other: Polynom) -> Polynom:
    
    warnings.warn('divide это всего лишь черновик функции')
    
    if other.is_null():
        raise ZeroDivisionError
    if self.degree < other.degree:
        return Polynom([Rational("0")])
    
    a = self.copy()
    b = other.copy()
    
    result = Polynom([Rational("0")])
    while a.degree() >= b.degree():
        coefficient = a[-1] / b[-1]
        result += Polynom([coefficient]).multiply_by_monomial(a.degree - b.degree)
        a -= b.multiply_by_scalar(coefficient)
    return result
