# Модуль: GCF_NN_N
# Автор: Мавликаев_Иван_2381

#НОД многочленов

from .Polynom import Polynom

def DCF(self: Polynom, other: Polynom)-> Polynom:
    pol1 = self.copy()
    pol2 = other.copy()

    while pol1.get_degree() > 0 and pol2.get_degree() > 0:
        if pol1.get_degree() > pol2.get_degree():
            pol1 = pol1.mod(pol2)
        else:
            pol2 = pol2.mod(pol1)
    if pol1.get_degree() == 0:
        return pol2
    else:
        return pol1