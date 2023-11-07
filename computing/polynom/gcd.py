# Модуль: GCF_PP_P
# Автор: Мавликаев_Иван_2381

#НОД многочленов
from .Polynom import Polynom


def gcd(self: Polynom, other: Polynom)-> Polynom:
    pol1 = self.copy()
    pol2 = other.copy()
    deg1 = pol1.get_degree()
    deg2 = pol2.get_degree()
    while deg1 > 0 and deg2 > 0:
        if deg1 > deg2:
            pol1 = pol1.mod(pol2)
            deg1 = pol1.get_degree()
        else:
            pol2 = pol2.mod(pol1)
            deg2 = pol2.get_degree()
    if deg1 == 0:
        return pol2
    return pol1
