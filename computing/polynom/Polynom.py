from computing.natural.Natural import Natural
from computing.integer.Integer import Integer
from computing.rational.Rational import Rational


class Polynom:
    data: list[Rational]
    degree: int

    def __init__(self, value: list[Rational]) -> None:
        if value == []:
            self.data = [Rational("0")]
            return
        self.data = value
        while len(self.data) > 1 and self.data[-1] == Rational("0"):
            self.data.pop()

    def __str__(self):
        s = ", ".join(str(x) for x in self.data)
        return f"[{s}]"

    def __repr__(self):
        return f"Polynom({self})"

    def get_degree(self):
        from .get_degree import get_degree
        return get_degree(self)

    def get_leading_coefficient(self):
        from .get_leading_coefficient import get_leading_coefficient
        return get_leading_coefficient(self)
