# Автор: Рыжиков_Иван_2381
from computing.integer.Integer import Integer


def test_555():
    s = "555"
    a = Integer(s)
    assert str(a) == s


def test_1488():
    s = "1488"
    a = Integer(s)
    assert str(a) == s


def test_m555():
    s = "-555"
    a = Integer(s)
    assert str(a) == s


def test_m228():
    s = "-228"
    a = Integer(s)
    assert str(a) == s


def test_0():
    s = "0"
    a = Integer(s)
    assert str(a) == s
