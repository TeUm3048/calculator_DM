# Модуль: FAC_P_Q
# Автор: Комосский_Егор_2381

from computing.polynom.Polynom import Polynom
from computing.natural.Natural import Natural
from computing.rational.Rational import Rational
from computing.integer.Integer import Integer


def factor_polynomial_coefficients(self: Polynom) -> Polynom:
    nk = self.data[0].denominator
    nd = self.data[0].numerator.absolute()
    for i in range(len(self.data)):
        nk = Natural.lcm(nk, self.data[i].denominator)
        nd = Natural.gcd(nd, self.data[i].numerator.absolute())
    ans = [Rational.simplify(Rational.multiply(i, Rational([Integer.from_natural(nk), nd]))) for i in self.data]
    return Polynom(ans)

