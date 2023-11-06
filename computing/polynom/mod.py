# Модуль: MOD_PP_P
# Автор: Кузнецов_Илья_2381

from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational


def mod(pol1: Polynom, pol2: Polynom) -> Polynom:
    num1 = pol1.copy()
    num2 = pol2.copy()

    return num1.subtract(num2.multiply(num1.divide(num2)))

