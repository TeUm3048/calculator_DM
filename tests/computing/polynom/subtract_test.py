#Автор: Кривов_Савелий_2381

from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational


def test_default():
    a = Polynom([Rational("-3/5"), Rational("-4"), Rational("10")])
    b = Polynom([Rational("6"), Rational("7"), Rational("9")])

    correct_res = Polynom([Rational("-33/5"), Rational("-11"), Rational("1")])
    res = a.subtract(b)

    assert str(res) == str(correct_res)


def test_0():
    a = Polynom([Rational("6"), Rational("-4"), Rational("10")])
    b = Polynom([Rational("6"), Rational("7"), Rational("9")])

    correct_res = Polynom([Rational("0"), Rational("-11"), Rational("1")])
    res = a.subtract(b)

    assert str(res) == str(correct_res)


def test_diff_len_1():
    a = Polynom([Rational("-3/5"), Rational("-4")])
    b = Polynom([Rational("6"), Rational("7"), Rational("-10")])

    correct_res = Polynom([Rational("-33/5"), Rational("-11"), Rational("10")])
    res = a.subtract(b)

    assert str(res) == str(correct_res)


def test_diff_len_2():
    a = Polynom([Rational("-3/5"), Rational("-4"), Rational("23")])
    b = Polynom([Rational("6"), Rational("7")])

    correct_res = Polynom([Rational("-33/5"), Rational("-11"), Rational("23")])
    res = a.subtract(b)

    assert str(res) == str(correct_res)
