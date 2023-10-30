# Автор: Кузнецов_Илья_2381
from computing.natural.Natural import Natural


def multiply_by_power_of_10_correct(num: Natural, k: Natural) -> Natural:
    return Natural(str(int(num) * (10 ** int(k))))


def test_default():
    a = Natural(str(3113))
    k = Natural(str(3))
    correct_res = multiply_by_power_of_10_correct(a, k)
    res = a.multiply_by_power_of_10(k)
    assert str(res) == str(correct_res)


def test_k_equal_zero():
    a = Natural(str(3113))
    k = Natural(str(0))
    correct_res = multiply_by_power_of_10_correct(a, k)
    res = a.multiply_by_power_of_10(k)
    assert str(res) == str(correct_res)


def test_k_more_num():
    a = Natural(str(3))
    k = Natural(str(10))
    correct_res = multiply_by_power_of_10_correct(a, k)
    res = a.multiply_by_power_of_10(k)
    assert str(res) == str(correct_res)


def test_k_and_num_zero():
    a = Natural(str(0))
    k = Natural(str(0))
    correct_res = multiply_by_power_of_10_correct(a, k)
    res = a.multiply_by_power_of_10(k)
    assert str(res) == str(correct_res)
