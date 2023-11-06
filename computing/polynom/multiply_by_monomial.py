# Модуль: MUL_Pxk_P
# Авторка: 

from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational
from computing.natural.Natural import Natural


def multiply_by_monomial(self: Polynom, k: "int | Natural") -> Polynom:

    if self.is_null():
        return self.copy()

    if isinstance(k, int):
        result = self.copy()
        result.data = [Rational("0") for i in range(k)] + result.data
        return result
    
    result = Polynom.copy()
    power = k.copy()
    one = Rational("1")
    while power.is_not_zero():
        result.data = [Rational("0")] + result.data
        power.subtract(one)
    return result
