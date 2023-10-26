# Автор: Ярослав_Ваньков_2382

from computing.natural.Natural import Natural


def test_first_more():
    num1 = Natural('321')
    num2 = Natural('123')
    assert num1.compare(num2) == 2


def test_first_less():
    num1 = Natural('321')
    num2 = Natural('123')
    assert num2.compare(num1) == 1


def test_equal():
    num1 = Natural('321')
    num2 = Natural('321')
    assert num2.compare(num1) == 0
