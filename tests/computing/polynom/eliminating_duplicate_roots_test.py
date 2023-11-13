from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational


def test_example():
    # (x-1) * (x-2)^2 * (x-3)^3 =
    # 108 - 324 x + 387 x^2 - 238 x^3 + 80 x^4 - 14 x^5 + x^6
    a = Polynom([Rational("108"), Rational("-324"), Rational("387"), Rational("-238"),
                 Rational("80"), Rational("-14"), Rational("1")])
    b = a.eliminating_duplicate_roots()
    # (x-1) * (x-2)^2 * (x-3)^3 = -6 + 11x - 6x^2 + x^3
    curr_res = Polynom([Rational("6"), Rational("-11"), Rational("6"), Rational("-1")])
    assert b == curr_res


def test_1():
    # 1 - 2x + x^2
    a = Polynom([Rational("1"), Rational("-2"), Rational("1")])

    b = a.eliminating_duplicate_roots()
    assert b == Polynom([Rational("-1"), Rational("1")])


def test_2():
    # -6 + 11x - 6x^2 + x^3
    a = Polynom([Rational("-6"), Rational("11"), Rational("-6"), Rational("1")])
    curr_res = a.copy()
    b = a.eliminating_duplicate_roots()
    assert b == curr_res


def test_zero():
    # -6 + 11x - 6x^2 + x^3
    a = Polynom([Rational("0")])
    curr_res = a.copy()

    b = a.eliminating_duplicate_roots()
    assert b == curr_res


def test_monomial():
    # -6 + 11x - 6x^2 + x^3
    a = Polynom([Rational("0"), Rational("5")])
    curr_res = a.copy()

    b = a.eliminating_duplicate_roots()
    assert b == curr_res
