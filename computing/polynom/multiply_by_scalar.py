# Модуль: MOD_PP_P
# Автор: Ваньков_Ярослав_2381

from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational


def multiply_by_scalar(pol1: Polynom, scalar: Rational) -> Polynom:
    pol = pol1.copy()
    for i in range(len(pol)):
        pol.data[i] = pol.data[i].multiply(scalar)
    return pol
