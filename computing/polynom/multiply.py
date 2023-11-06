# Модуль: MUL_PP_P
# Автор: Потапова_Дарья_2381


from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational


def multiply(poly1: Polynom, poly2: Polynom) -> Polynom:
    result = Polynom([Rational("0")])
    pol1 = poly1.copy()
    pol2 = poly2.copy()
    for i in range(pol2.get_degree() + 1):
        added = pol1.multiply_by_monomial(i)
        result = result.add(added.multiply_by_scalar(pol2.data[i]))
    return result


