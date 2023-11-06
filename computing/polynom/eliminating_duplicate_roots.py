from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational

def eliminating_duplicate_roots(self: Polynom):
    f_der = self.derive()
    d = self.gcd(f_der)
    return self.divide(d)
