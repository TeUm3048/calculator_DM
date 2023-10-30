# Автор: Ваньков_Ярослав_2382

from computing.natural.Natural import Natural


def is_not_zero_correct(self: Natural) -> bool:
    return self != Natural('0')


def test_zero():
    num1 = Natural('0')
    assert num1.is_not_zero() == is_not_zero_correct(num1)


def test_not_zero():
    num1 = Natural('321')
    assert num1.is_not_zero() == is_not_zero_correct(num1)


def test_end_zero():
    num1 = Natural('1000')
    assert num1.is_not_zero() == is_not_zero_correct(num1)
