# Модуль: FAC_P_Q
# Автор: Комосский_Егор_2381

from computing.polynom.Polynom import Polynom
from computing.natural.Natural import Natural
from computing.rational.Rational import Rational
from computing.integer.Integer import Integer

# Факторизация коэфициентов многочлена
def factor_polynomial_coefficients(self: Polynom) -> Polynom:
    # Для подсчёта НОК и НОД записываем знаменатель и числитель первого коэффициента
    nk = self.data[0].denominator
    # Если первый коэф. равен 0, то записываем 1, чтобы функция подсчёта НОД работала корректно
    nd = self.data[0].numerator.absolute() if self.data[0].numerator.absolute() != Natural('0') else Natural('1')
    # Проходимся в цикле по всем коэф-ам многочлена и рассчитываем НОК и НОД
    for i in range(len(self.data)):
        nk = Natural.lcm(nk, self.data[i].denominator)
        nd = Natural.gcd(nd, self.data[i].numerator.absolute()) if \
            self.data[i].numerator.absolute() != Natural('0') else nd
    # Домножаем все коэф-ты на НОК и делим на НОД
    ans = [Rational.simplify(Rational.multiply(i, Rational([Integer.from_natural(nk), nd]))) for i in self.data]
    return Polynom(ans)
