from computing.integer.Integer import Integer


def test_str():
    s = Integer("5")
    assert str(s) == "5"
