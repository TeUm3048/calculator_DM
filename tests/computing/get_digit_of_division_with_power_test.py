import pytest

from computing.natural.Natural import Natural


def correct(a: Natural, b: Natural) -> Natural:
    res = str(int(a) // int(b))
    a000000 = res[0] + "0" * (len(res) - 1)
    return Natural(a000000)


def test_default():
    for i in range(1, 200):
        for j in range(1, 200):
            a = Natural(str(i))
            b = Natural(str(j))
            assert (a.get_digit_of_division_with_power(b), a, b
                    ) == (correct(a, b), a, b)


def test_11_1():
    a = Natural("11")
    b = Natural("1")
    assert a.get_digit_of_division_with_power(b) == correct(a, b)


def test_div_by_2():
    a = Natural("234")
    assert a.get_digit_of_division_with_power(Natural("2")) == Natural("100")


def test_div_by_1():
    a = Natural("814365")
    b = Natural("1")
    assert a.get_digit_of_division_with_power(b) == Natural("800000")


def test_div_by_27():
    a = Natural("814365")
    b = Natural("27")
    assert a.get_digit_of_division_with_power(b) == Natural("30000")


def test_div_by_555():
    a = Natural("25")
    b = Natural("555")
    assert a.get_digit_of_division_with_power(b) == Natural("0")


def test_div_by_0():
    a = Natural("435")
    b = Natural("0")
    with pytest.raises(ZeroDivisionError):
        a.get_digit_of_division_with_power(b)
