import pytest

from computing.natural.Natural import Natural


def div_correct(num1: Natural, num2: Natural) -> Natural:
    return Natural(str(int(num1) // int(num2)))


def test_div_12_by_3():
    a = Natural("12")
    b = Natural("3")
    res = a // b
    assert res == div_correct(a, b)


def test_div_14_by_3():
    a = Natural("14")
    b = Natural("3")
    res = a // b
    assert res == div_correct(a, b)


def test_div_0_by_3():
    a = Natural("0")
    b = Natural("3")
    res = a // b
    assert res == div_correct(a, b)


def test_div_by_0():
    a = Natural("12")
    b = Natural("0")
    with pytest.raises(ZeroDivisionError):
        res = a // b
