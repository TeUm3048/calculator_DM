from computing.integer.Integer import Integer
from computing.natural.Natural import Natural
from computing.rational.Rational import Rational
from computing.polynom.Polynom import Polynom

class NaturalModel:
    def __init__(self, num: Natural):
        self.type = "natural"
        self.num = str(num)


class IntegerModel:
    def __init__(self, num: Integer):
        self.type = "integer"
        self.num = str(num)


class RationalModel:
    def __init__(self, num: Rational):
        self.type = "rational"
        self.num = str(num)


class PolynomModel:
    def __init__(self, num: Polynom):
        self.type = "polynom"
        self.num = list(map(str, num.data))
