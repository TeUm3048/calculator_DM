# Автор: Мавликаев_Иван_2381
import pytest
from computing.integer.Integer import Integer


def test_12_6():
    a = Integer("12")
    b = Integer("6")
    assert a.div(b) == Integer("2")


def test_150_72():
    a = Integer("-150")
    b = Integer("72")
    assert a.div(b) == Integer("-2")


def test_155_10():
    a = Integer("-155")
    b = Integer("-10")
    assert a.div(b) == Integer("15")


def test_155_200():
    a = Integer("155")
    b = Integer("-200")
    assert a.div(b) == Integer("0")



def test_155_0():
    a = Integer("155")
    b = Integer("0")
    with pytest.raises(ZeroDivisionError):
        a.div(b)