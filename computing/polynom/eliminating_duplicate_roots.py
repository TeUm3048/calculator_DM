from computing.polynom.Polynom import Polynom

# Сокращение кратных корней
def eliminating_duplicate_roots(self: Polynom):
    # Нахождение производной многочлена
    f_der = self.derive()
    # Нахождение НОД многочлена и его производной
    d = self.gcd(f_der)
    # Выводим результат деления многочлена на d
    return self.divide(d)
