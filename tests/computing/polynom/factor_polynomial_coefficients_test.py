#Автор: Комосский_Егор_2381

from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational


def test_2__2_5__23_81():
    p = Polynom([Rational('2'), Rational('3/5'), Rational('23/81')])
    assert str(p.factor_polynomial_coefficients()) == str(Polynom([Rational('810'), Rational('243'), Rational('115')]))


def test_0():
    p = Polynom([Rational('0'), Rational('1')])
    assert str(p.factor_polynomial_coefficients()) == str(Polynom([Rational('0'), Rational('1')]))


def test_negative():
    p = Polynom([Rational('-4'), Rational('8/9'), Rational('-24/25')])
    assert str(p.factor_polynomial_coefficients()) == str(Polynom([Rational('-225'), Rational('50'), Rational('-54')]))

