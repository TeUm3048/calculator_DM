from computing.Integer import Integer


def test_str():
    s = "-5462"
    assert str(Integer(s)) == s


