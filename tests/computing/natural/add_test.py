# Автор: Ярослав_Ваньков_2382
from computing.natural.Natural import Natural


def add_correct(self: Natural, other: Natural) -> Natural:
    return Natural(str(int(self)+int(other)))


def test_default():
    for i in range(0, 100):
        for j in range(0, 100):
            a = Natural(str(i))
            b = Natural(str(j))
            correct_res = add_correct(a, b)
            res = a.add(b)
            assert str(res) == str(correct_res)


def test_zero():
    zero = Natural('0')
    assert str(add_correct(zero, zero)) == str(zero.add(zero))

