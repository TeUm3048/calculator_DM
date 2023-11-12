from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational


def test_gcd_1():
    a = Polynom([Rational("1"), Rational("2"), Rational("1")])
    b = Polynom([Rational("1"), Rational("1")])
    assert a.gcd(b) == Polynom([Rational("1"), Rational("1")])


def test_gcd_2():
    a = Polynom([Rational("6"), Rational("5"), Rational("1")])
    b = Polynom([Rational("3"), Rational("1")])
    assert a.gcd(b) == Polynom([Rational("3"), Rational("1")])


def test_gcd_3():
    # ( 5+4 x) (x + 2)
    a = Polynom([Rational("10"), Rational("13"), Rational("4")])
    # (35 + 28x)
    b = Polynom([Rational("35"), Rational("28")])
    assert a.gcd(b) == Polynom([Rational("5"), Rational("4")])


def test_gcd_4():
    # (x-1)(x-2)(x-3)
    a = Polynom([Rational("-6"), Rational("11"), Rational("-6"), Rational("1")])
    # Have no root
    b = Polynom([Rational("11"), Rational("-12"), Rational("3")])
    assert a.gcd(b) == Polynom([Rational("1")])



