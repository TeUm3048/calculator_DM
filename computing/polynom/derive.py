# Модуль: DER_P_P
# Автор: Газукина_Дарья_2381

from .Polynom import Polynom
from computing.rational.Rational import Rational

def derive (pol: Polynom) -> Polynom:
    derivative = pol.copy()
    for i in range(len(derivative)-1):
        derivative.data[i] = derivative.data[i+1]
        degree = Rational(str(i + 1) + '/1')
        derivative.data[i] = derivative.data[i] * degree
    derivative.data.pop(-1)
    return derivative
