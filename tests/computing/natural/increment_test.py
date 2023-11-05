# Автор: Ваньков_Ярослав_2382
from computing.natural.Natural import Natural


def increment_correct(self: Natural) -> None:
    self.data = Natural(str(int(self)+1)).data


def test_default():
    num1 = Natural('1321')
    assert increment_correct(num1) == num1.increment()


def test_zero():
    num1 = Natural('0')
    num1.increment()
    assert Natural('1') == num1


def test_999():
    num1 = Natural('999')
    num1.increment()
    assert Natural('1000') == num1


def test_no_default():
    num1 = Natural('789')
    num1.increment()
    assert Natural('709') != num1


def test_9():
    num1 = Natural('9')
    num1.increment()
    assert Natural('10') == num1
