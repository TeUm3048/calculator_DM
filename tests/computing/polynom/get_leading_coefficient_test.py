# Автор: Богатов_Илья_2381

import pytest
from computing.rational.Rational import Rational
from computing.polynom.Polynom import Polynom


def test_get_leading_coefficient():
    p = Polynom([Rational('1/2'), Rational('2/3'), Rational('3/4')])
    assert p.get_leading_coefficient() == Rational('3/4')

    p = Polynom([Rational('1/2'), Rational('0'), Rational('2/3')])
    assert p.get_leading_coefficient() == Rational('2/3')

    p = Polynom([Rational('0')])
    assert p.get_leading_coefficient() == Rational('0')

    p = Polynom([])
    assert p.get_leading_coefficient() == Rational('0')
