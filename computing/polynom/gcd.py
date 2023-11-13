# Модуль: GCF_PP_P
# Автор: Мавликаев_Иван_2381

#НОД многочленов
from .Polynom import Polynom
from computing.rational.Rational import Rational


def gcd(self: Polynom, other: Polynom)-> Polynom:
    pol1 = self.copy()
    pol2 = other.copy()
    deg1 = pol1.get_degree()
    deg2 = pol2.get_degree()
    while not pol1.is_null() and not pol2.is_null():
        if deg1 > deg2 or deg1 == deg2 and pol1.data[-1] > pol2.data[-1]:
            pol1 = pol1.mod(pol2)
            deg1 = pol1.get_degree()
        else:
            pol2 = pol2.mod(pol1)
            deg2 = pol2.get_degree()
    if pol1.is_null():
        if deg2 == 0 and pol2.data[0] < Rational("0"):
            pol2 = pol2.multiply_by_scalar(Rational("-1"))
        return pol2
    if deg1 == 0 and pol1.data[0] < Rational("0"):
        pol1 = pol1.multiply_by_scalar(Rational("-1"))
    return pol1
