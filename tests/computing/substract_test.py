# Автор: Кузнецов_Илья_2381
from computing.natural.Natural import Natural
import pytest


def subtract_correct(num1: Natural, num2: Natural) -> Natural:
    if int(num1) < int(num2):
        raise ValueError
    return Natural(str(int(num1) - int(num2)))


def test_default_1():
    a = Natural(str(31453))
    b = Natural(str(122))
    correct_res = subtract_correct(a, b)
    res = a.subtract(b)
    assert str(res) == str(correct_res)


def test_default_2():
    a = Natural(str(31453243))
    b = Natural(str(121232))
    correct_res = subtract_correct(a, b)
    res = a.subtract(b)
    assert str(res) == str(correct_res)


def test_default_3():
    a = Natural(str(31412353))
    b = Natural(str(121232))
    correct_res = subtract_correct(a, b)
    res = a.subtract(b)
    assert str(res) == str(correct_res)


def test_by_zero():
    a = Natural(str(31453))
    b = Natural(str(0))
    correct_res = subtract_correct(a, b)
    res = a.subtract(b)
    assert str(res) == str(correct_res)


def test_by_equal():
    a = Natural(str(31453))
    b = Natural(str(31453))
    correct_res = subtract_correct(a, b)
    res = a.subtract(b)
    assert str(res) == str(correct_res)


def test_more_by_less():
    a = Natural(str(31412))
    b = Natural(str(1213))
    correct_res = subtract_correct(a, b)
    res = a.subtract(b)
    assert str(res) == str(correct_res)


def test_less_by_more():
    a = Natural(str(123))
    b = Natural(str(123213))
    with pytest.raises(ValueError):
        correct_res = subtract_correct(a, b)
        res = a.subtract(b)
    assert str(res) == str(correct_res)


def test_zero_by_zero():
    a = Natural(str(0))
    b = Natural(str(0))
    correct_res = subtract_correct(a, b)
    res = a.subtract(b)
    assert str(res) == str(correct_res)
