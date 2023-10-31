import pytest

from computing.natural.Natural import Natural


def correct(num1: Natural, num2: Natural) -> Natural:
    return Natural(str(int(num1) // int(num2)))


def test_default():
    for i in range(1, 1000):
        for j in range(1, 100):
            a = Natural(str(i))
            b = Natural(str(j))
            assert (a // b, a, b) == (correct(a, b), a, b)


def test_div_76_25():
    a = Natural("76")
    b = Natural("25")
    res = a // b
    assert res == correct(a, b)


def test_div_100_25():
    a = Natural("100")
    b = Natural("25")
    res = a // b
    assert res == correct(a, b)


def test_div_12_by_3():
    a = Natural("12")
    b = Natural("3")
    res = a // b
    assert res == correct(a, b)


def test_div_14_by_3():
    a = Natural("14")
    b = Natural("3")
    res = a // b
    assert res == correct(a, b)


def test_div_0_by_3():
    a = Natural("0")
    b = Natural("3")
    res = a // b
    assert res == correct(a, b)


def test_div_by_0():
    a = Natural("12")
    b = Natural("0")
    with pytest.raises(ZeroDivisionError):
        res = a // b
