from computing.polynom.Polynom import Polynom


def eliminating_duplicate_roots(self: Polynom):
    f_der = self.derive()
    d = self.gcd(f_der)
    return self.divide(d)
