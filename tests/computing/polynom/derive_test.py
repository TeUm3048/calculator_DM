# Автор: Газукина_Дарья_2381
from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational


def test_1():
    # 5 x^4 - 6 x^3 + 4 x + 5
    # derive(5x^0 + 4x^1 + 0x^2 - 6x^3 + 5x^4) = 4x^0 - 18x^2 + 20x^3
    a = Polynom([Rational("5"), Rational("4"), Rational("0"), Rational("-6"), Rational("5")])
    b = a.derive()
    # 4x^0 - 18x^2 + 20x^3
    curr_res = Polynom([Rational("4"), Rational("0"), Rational("-18"), Rational("20")])
    assert str(b) == str(curr_res)


def test_2():
    # 3x^0  + 4x^1  + 1x^2  + 7x^3  + 0x^4  + 8x^5  + -10x^6  + 4x^7
    a = Polynom([Rational("3"), Rational("4"), Rational("1"), Rational("7"), Rational("0"),
                 Rational("8"), Rational("-10"), Rational("4")])
    b = a.derive()
    # 4x^0  + 2x^1  + 21x^2  + 0x^3  + 40x^4  + -60x^5  + 28x^6
    curr_res = Polynom([Rational("4"), Rational("2"), Rational("21"), Rational("0"),
                        Rational("40"), Rational("-60"), Rational("28")])
    assert str(b) == str(curr_res)


def test_zero():
    # 0x^0  + 1x^1  + 0x^2
    a = Polynom([Rational("0"), Rational("1"), Rational("0")])
    b = a.derive()
    # 1x^0  + 0x^1
    curr_res = Polynom([Rational("1"), Rational("0")])
    assert str(b) == str(curr_res)


def test_degree_0():
    # 4x^0
    a = Polynom([Rational("4")])
    b = a.derive()
    # 0x^0
    curr_res = Polynom([Rational("0")])
    assert str(b) == str(curr_res)
