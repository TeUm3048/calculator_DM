# Автор: Комосский_Егор_2381
from computing.integer.Integer import Integer


def sub_correct(self: Integer, other: Integer) -> Integer:
    return Integer(str(int(self) - int(other)))


def test_default():
    for i in range(-100, 100):
        for j in range(-100, 100):
            a = Integer(str(i))
            b = Integer(str(j))
            correct_res = sub_correct(a, b)
            res = a.subtract(b)
            assert str(res) == str(correct_res)
