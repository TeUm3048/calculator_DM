from Rational import Rational


class Polynom:
    data: list[Rational]
    degree: int
    pass

    def get_degree(self):
        from .get_degree import get_degree
        return get_degree(self)
