# Автор: Кузнецов_Илья_2381
from computing.natural.Natural import Natural, Digit
import pytest


def substract_product_from_natural_correct(num1: Natural, num2: Natural,
                                           k: Digit) -> Natural:
    return Natural(str(int(num1) - int(num2) * k))


def test_default():
    num1 = Natural(str(123123211221))
    num2 = Natural(str(12312321))
    k = 5
    correct_res = substract_product_from_natural_correct(num1, num2, k)
    res = num1.subtract_product_from_natural(num2, k)
    assert str(correct_res) == str(res)


def test_minus_result():
    num1 = Natural(str(12312321))
    num2 = Natural(str(123123211221))
    k = 5
    with pytest.raises(ValueError):
        res = num1.subtract_product_from_natural(num2, k)


def test_zero():
    num1 = Natural(str(100000))
    num2 = Natural(str(100000))
    k = 1
    correct_res = substract_product_from_natural_correct(num1, num2, k)
    res = num1.subtract_product_from_natural(num2, k)
    assert str(correct_res) == str(res)


def test_zero_k():
    num1 = Natural(str(100000))
    num2 = Natural(str(1001231201230))
    k = 0
    correct_res = substract_product_from_natural_correct(num1, num2, k)
    res = num1.subtract_product_from_natural(num2, k)
    assert str(correct_res) == str(res)


def test_zero_num1_num2():
    num1 = Natural(str(0))
    num2 = Natural(str(0))
    k = 6
    correct_res = substract_product_from_natural_correct(num1, num2, k)
    res = num1.subtract_product_from_natural(num2, k)
    assert str(correct_res) == str(res)


def test_all_zero():
    num1 = Natural(str(0))
    num2 = Natural(str(0))
    k = 0
    correct_res = substract_product_from_natural_correct(num1, num2, k)
    res = num1.subtract_product_from_natural(num2, k)
    assert str(correct_res) == str(res)
