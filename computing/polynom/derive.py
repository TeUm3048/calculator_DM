# Модуль: DER_P_P
# Автор: Газукина_Дарья_2381

from .Polynom import Polynom
from computing.rational.Rational import Rational

def derive (pol: Polynom) -> Polynom:
    derivative = pol.copy()
    for i in range(len(derivative.data)-1):
        derivative.data[i] = derivative.data[i+1]
        degree = Rational(str(i + 1) + '/1')
        # degree = Rational([i + 1, 1])
        derivative.data[i] = derivative.data[i].multiply(degree)
    derivative.data.pop(-1)
    return derivative

# if __name__ == '__main__':
#     a = Polynom([Rational("5"), Rational("4"), Rational("0"), Rational("-6"), Rational("5")])
#     b = a.derive()
#     curr_res = Polynom([Rational("4"), Rational("-18"), Rational("20")])
