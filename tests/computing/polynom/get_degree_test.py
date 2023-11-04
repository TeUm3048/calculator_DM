# Автор: Богатов_Илья_2381

import pytest
from computing.rational.Rational import Rational
from computing.polynom.Polynom import Polynom


def test_get_degree():
    p = Polynom([Rational('1/2'), Rational('2/3'), Rational('3/4')])
    assert p.get_degree() == 2

    p = Polynom([])
    assert p.get_degree() == -1
