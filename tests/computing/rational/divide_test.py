# Автор: Ильясов_Марк_2381

from computing.rational.Rational import Rational
from tests.computing.rational.generate_rationals import generate_rationals

MAX_FLOAT_ERROR = 0.000_000_1

def check_divide(a: Rational, b: Rational):
    if b == Rational("0"):
        try:
            c = a / b
        except ZeroDivisionError:
            return True
        else:
            return False
    
    res = float(a / b)
    correct = float(a) / float(b)
    return abs(res - correct) <= MAX_FLOAT_ERROR

def test_default():
    rationals = generate_rationals()
    for a in rationals:
        for b in rationals:
            assert check_divide(a, b)