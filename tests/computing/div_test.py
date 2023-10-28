from computing.natural.Natural import Natural


def test_div_12_by_3():
    a = Natural("12")
    b = Natural("3")
    res = a // b
    assert res == Natural("4")
