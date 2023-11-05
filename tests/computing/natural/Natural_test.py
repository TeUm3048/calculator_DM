from computing.natural.Natural import Natural


def test_compare_less():
    a = Natural("6")
    b = Natural("5555")
    assert a.compare(b) == 1


def test_compare_more():
    a = Natural("666")
    b = Natural("7")
    assert a.compare(b) == 2


def test_compare_equal():
    a = Natural("17")
    b = Natural("17")
    assert a.compare(b) == 0


# def test_div_1():
#     assert Natural("4") // Natural("2") == str(Natural("2"))


# def test_div_2():
#     assert Natural("4").div(Natural("2")) == str(Natural("2"))


def test_str():
    s = "5462"
    assert str(Natural(s)) == s
