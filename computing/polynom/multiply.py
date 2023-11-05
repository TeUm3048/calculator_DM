# Модуль: MUL_PP_P
# Автор: Потапова_Дарья_2381


from .Polynom import Polynom
from computing.rational.Rational import Rational


def multiply (poly1: Polynom, poly2: Polynom) -> Polynom:
    result = Polynom([Rational("0")])
    for i in range(len(poly1.data) + len(poly2.data) - 2):
        result.data.append(Rational("0"))
    for i in range(len(poly1.data)):
        for j in range(len(poly2.data)):
            result.data[i + j] = result.data[i + j].add(poly1.data[i].multiply(poly2.data[j]))
    return result
