# Автор: Рыжиков_Иван_2381
from computing.integer.Integer import Integer


def test_123():
    a = 123
    b = Integer(str(a))
    assert int(b) == a


def test_m123():
    a = -123
    b = Integer(str(a))
    assert int(b) == a


def test_0():
    a = 0
    b = Integer(str(a))
    assert int(b) == a
