# Автор: Потапова_Дарья_2381

import pytest
from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational


def test_1():
    a = Polynom([Rational("3"), Rational("7"), Rational("4")])
    b = Polynom([Rational("1"), Rational("2"), Rational("3")])
    c = a.multiply(b)
    curr_res = Polynom([Rational("3"), Rational("13"), Rational("27"), Rational("29"), Rational("12")])
    assert str(c) == str(curr_res)


def test_2():
    a = Polynom([Rational("3")])
    b = Polynom([Rational("1"), Rational("2"), Rational("3")])
    c = a.multiply(b)
    curr_res = Polynom([Rational("3"), Rational("6"), Rational("9")])
    assert str(c) == str(curr_res)


def test_3():
    a = Polynom([Rational("3")])
    b = Polynom([Rational("6")])
    c = a.multiply(b)
    curr_res = Polynom([Rational("18")])
    assert str(c) == str(curr_res)


def test_4():
    a = Polynom([Rational("-3"), Rational("-3"), Rational("0"), Rational("1"), Rational("0"), Rational("1")])
    b = Polynom([Rational("5"), Rational("0"), Rational("3")])
    c = a.multiply(b)
    curr_res = Polynom([Rational("-15"), Rational("-15"), Rational("-9"), Rational("-4"),
                        Rational("0"), Rational("8"), Rational("0"), Rational("3")])
    assert str(c) == str(curr_res)


