# Модуль: ADD_QQ_Q
# Автор: Комосский_Егор_2381

from computing.rational.Rational import Rational
from computing.integer.Integer import Integer


# Сложение двух чисел
def add(self: Rational, other: Rational) -> Rational:

    # Инициализация двух чисел на основе переданных в функцию
    num1 = self.copy()
    num2 = other.copy()

    # Нахождение наименьшего общего кратного переданных чисел
    lcm = num1.denominator.lcm(num2.denominator)

    # Сложение чисел
    new_numer = (num1.numerator.multiply(Integer.from_natural(
        lcm.div(num1.denominator)))).add(
        num2.numerator.multiply(
            Integer.from_natural(lcm.div(num2.denominator))))

    # Создание, упрощение и возврат нового числа
    return Rational([new_numer, lcm]).simplify()
