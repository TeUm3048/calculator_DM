from computing.rational.Rational import Rational
from computing.integer.Integer import Integer
from computing.natural.Natural import Natural

def generate_rationals():
    rationals = []
    for i in range(-11, 11):
        for j in range(1, 7):
            numerator = Integer(str(i))
            denominator = Natural(str(j))
            rationals.append(Rational([numerator, denominator]))
    return rationals