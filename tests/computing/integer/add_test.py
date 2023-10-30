# Автор: Комосский_Егор_2381
from computing.integer.Integer import Integer


def add_correct(self: Integer, other: Integer) -> Integer:
    return Integer(str(int(self) + int(other)))


def test_default():
    for i in range(-100, 100):
        for j in range(-100, 100):
            a = Integer(str(i))
            b = Integer(str(j))
            correct_res = add_correct(a, b)
            res = a.add(b)
            assert str(res) == str(correct_res)


def test_m100_1():
    a = Integer("-100")
    b = Integer("1")
    correct_res = add_correct(a, b)
    res = a.add(b)
    assert str(res) == str(correct_res)


def test_m99_0():
    a = Integer("-99")
    b = Integer("0")
    correct_res = add_correct(a, b)
    res = a.add(b)
    assert str(res) == str(correct_res)


def test_0_m99():
    a = Integer("0")
    b = Integer("-99")
    correct_res = add_correct(a, b)
    res = a.add(b)
    assert str(res) == str(correct_res)


def test_zero():
    zero = Integer('0')
    assert str(add_correct(zero, zero)) == str(zero.add(zero))
