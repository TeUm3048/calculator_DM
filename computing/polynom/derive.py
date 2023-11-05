# Модуль: DER_P_P
# Автор: Газукина_Дарья_2381

from .Polynom import Polynom
from computing.rational.Rational import Rational

def derive (pol: Polynom) -> Polynom:
    derivative = pol.copy()
    if len(derivative.data) > 1:
        for i in range(len(derivative.data)-1):
            derivative.data[i] = derivative.data[i+1]
            degree = Rational(str(i + 1))
            derivative.data[i] = derivative.data[i].multiply(degree)
        derivative.data.pop(-1)
    else:
        derivative.data[0] = Rational('0')

    return derivative
