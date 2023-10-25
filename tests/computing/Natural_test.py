from computing.Natural import Natural


def test_div_1():
    assert Natural("4") // Natural("2") == str(Natural("2"))


def test_div_2():
    assert Natural("4").div(Natural("2")) == str(Natural("2"))


def test_str():
    s = "5462"
    assert str(Natural(s)) == s
