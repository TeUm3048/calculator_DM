# Автор: Кузнецов_Илья_2381
from computing.natural.Natural import Natural
from computing.natural.Natural import Digit


def multiply_by_digit_correct(num1: Natural, k: Digit) -> Natural:
    return Natural(str(int(num1) * k))


def test_default():
    a = Natural(str(31453))
    k = 7
    correct_res = multiply_by_digit_correct(a, k)
    res = a.multiply_by_digit(k)
    assert str(res) == str(correct_res)


def test_mult_by_zero_k():
    a = Natural(str(31453))
    k = 0
    correct_res = multiply_by_digit_correct(a, k)
    res = a.multiply_by_digit(k)
    assert str(res) == str(correct_res)


def test_mult_by_one():
    a = Natural(str(314213123))
    k = 1
    correct_res = multiply_by_digit_correct(a, k)
    res = a.multiply_by_digit(k)
    assert str(res) == str(correct_res)


def test_mult_by_nine():
    a = Natural(str(99999))
    k = 9
    correct_res = multiply_by_digit_correct(a, k)
    res = a.multiply_by_digit(k)
    assert str(res) == str(correct_res)


def test_mult_by_zero_num():
    a = Natural(str(0))
    k = 3
    correct_res = multiply_by_digit_correct(a, k)
    res = a.multiply_by_digit(k)
    assert str(res) == str(correct_res)


def test_mult_zero_by_zero():
    a = Natural(str(0))
    k = 0
    correct_res = multiply_by_digit_correct(a, k)
    res = a.multiply_by_digit(k)
    assert str(res) == str(correct_res)
