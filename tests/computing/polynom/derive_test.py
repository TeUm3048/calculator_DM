# Автор: Газукина_Дарья_2381
from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational

# def derive_correct(self: Polynom) -> Polynom:
#     pass


def test_default():
    # (x-1) * (x-2)^2 * (x-3)^3 =
    # 108 - 324 x + 387 x^2 - 238 x^3 + 80 x^4 - 14 x^5 + x^6
    # 5 x^4 - 6 x^3 + 4 x + 5
    # derive(5x^0 + 4x^1 + 0x^2 - 6x^3 + 5x^4) = 4x^0 - 18x^2 + 20x^3
    a = Polynom([Rational("5"), Rational("4"), Rational("0"), Rational("-6"), Rational("5")])
    b = a.derive()
    # (x-1) * (x-2)^2 * (x-3)^3 = -6 + 11x - 6x^2 + x^3
    curr_res = Polynom([Rational("4"), Rational("-18"), Rational("20")])
    assert str(b) == str(curr_res)


# def test_zero():
#     pass


# def test_example():
#     # (x-1) * (x-2)^2 * (x-3)^3 =
#     # 108 - 324 x + 387 x^2 - 238 x^3 + 80 x^4 - 14 x^5 + x^6
#     a = Polynom([Rational("108"), Rational("-324"), Rational("387"), Rational("-238"),
#                  Rational("80"), Rational("-14"), Rational("1")])
#     b = a.eliminating_duplicate_roots()
#     # (x-1) * (x-2)^2 * (x-3)^3 = -6 + 11x - 6x^2 + x^3
#     curr_res = Polynom([Rational("-6"), Rational("11"), Rational("-6"), Rational("1")])
#     assert str(b) == str(curr_res)


# def test_1():
#     # 1 - 2x + x^2
#     a = Polynom([Rational("1"), Rational("-2"), Rational("1")])
#
#     b = a.eliminating_duplicate_roots()
#     assert str(b) == str(Polynom([Rational("1"), Rational("-1")]))
#
#
# def test_2():
#     # -6 + 11x - 6x^2 + x^3
#     a = Polynom([Rational("-6"), Rational("11"), Rational("-6"), Rational("1")])
#
#     b = a.eliminating_duplicate_roots()
#     assert str(a) == str(b)