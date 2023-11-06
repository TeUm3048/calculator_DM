# Автор: Кузнецов_Илья_2381
import pytest

from computing.natural.Natural import Natural


def mod_correct(num1: Natural, num2: Natural) -> Natural:
    return Natural(str(int(num1) % int(num2)))


def test_default1():
    a = Natural(str(31453))
    b = Natural(str(1232))
    correct_res = mod_correct(a, b)
    res = a.mod(b)
    assert str(res) == str(correct_res)


def test_default2():
    a = Natural(str(31412312))
    b = Natural(str(1231232))
    correct_res = mod_correct(a, b)
    res = a.mod(b)
    assert str(res) == str(correct_res)


def test_default3():
    a = Natural(str(40000))
    b = Natural(str(2))
    correct_res = mod_correct(a, b)
    res = a.mod(b)
    assert str(res) == str(correct_res)


def test_second_bigger():
    a = Natural(str(1))
    b = Natural(str(1232))
    correct_res = mod_correct(a, b)
    res = a.mod(b)
    assert str(res) == str(correct_res)


def test_first_zero():
    a = Natural(str(0))
    b = Natural(str(1232))
    correct_res = mod_correct(a, b)
    res = a.mod(b)
    assert str(res) == str(correct_res)


def test_second_zero():
    with pytest.raises(ZeroDivisionError):
        a = Natural(str(123123))
        b = Natural(str(0))
        correct_res = mod_correct(a, b)
        res = a.mod(b)
        assert str(res) == str(correct_res)


def test_first_second_zero():
    with pytest.raises(ZeroDivisionError):
        a = Natural(str(0))
        b = Natural(str(0))
        correct_res = mod_correct(a, b)
        res = a.mod(b)
        assert str(res) == str(correct_res)
