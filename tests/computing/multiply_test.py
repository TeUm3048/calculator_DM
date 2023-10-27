# Автор: Кузнецов_Илья_2381
from computing.natural.Natural import Natural


def multiply_correct(num1: Natural, num2: Natural) -> Natural:
    return Natural(str(int(num1) * int(num2)))


def test_default():
    a = Natural(str(31453))
    b = Natural(str(122))
    correct_res = multiply_correct(a, b)
    res = a.multiply(b)
    assert str(res) == str(correct_res)


def test_multiply_by_one():
    a = Natural(str(10 ** 10))
    b = Natural(str(1))
    correct_res = multiply_correct(a, b)
    res = a.multiply(b)
    assert str(res) == str(correct_res)


def test_multiply_by_equal():
    a = Natural(str(10 ** 10))
    b = Natural(str(10 ** 10))
    correct_res = multiply_correct(a, b)
    res = a.multiply(b)
    assert str(res) == str(correct_res)


def test_multiply_by_zero():
    a = Natural(str(10 ** 10))
    b = Natural(str(0))
    correct_res = multiply_correct(a, b)
    res = a.multiply(b)
    assert str(res) == str(correct_res)


def test_zero_by_zero():
    a = Natural(str(0))
    b = Natural(str(0))
    correct_res = multiply_correct(a, b)
    res = a.multiply(b)
    assert str(res) == str(correct_res)
