# Автор: Ильясов_Марк_2381

from computing.rational.Rational import Rational
from computing.integer.Integer import Integer
from computing.natural.Natural import Natural
from tests.computing.rational.generate_rationals import generate_rationals

def equal_correct(a: Rational, b: Rational):
    return float(a) == float(b)

def less_correct(a: Rational, b: Rational):
    return float(a) < float(b)

def greather_correct(a: Rational, b: Rational):
    return float(a) > float(b)

def less_or_equal_correct(a: Rational, b: Rational):
    return float(a) <= float(b)

def greather_or_equal_correct(a: Rational, b: Rational):
    return float(a) >= float(b)

functions_and_correct_versions = {
    lambda a, b: a == b : equal_correct,
    lambda a, b: a < b : less_correct,
    lambda a, b: a > b : greather_correct,
    lambda a, b: a <= b : less_or_equal_correct,
    lambda a, b: a >= b : greather_or_equal_correct,
}


def test_default():
    rationals = generate_rationals()
    
    for a in rationals:
        for b in rationals:
            for func in functions_and_correct_versions:
                correct = functions_and_correct_versions[func]
                assert(str(a) and str(b) and func(a, b) == correct(a, b))
