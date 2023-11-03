from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational


def test_str_3_4_5():
    a = Polynom([Rational("3"), Rational("4"), Rational("5")])
    assert str(a) == "[3, 4, 5]"


def test_str_0():
    a = Polynom([Rational("0")])
    assert str(a) == "[0]"
