# Модуль: MUL_QQ_Q
# Автор: Комосский_Егор_2381

from computing.rational.Rational import Rational


# Умножение двух рациональных чисел
def multiply(self: Rational, other: Rational) -> Rational:

    # Инициализация двух чисел на основе переданных в функцию
    num1 = self.copy()
    num2 = other.copy()

    # Умножение, упрощение и возврат нового числа
    return Rational([num1.numerator.multiply(num2.numerator),
                     num1.denominator.multiply(num2.denominator)]).simplify()
