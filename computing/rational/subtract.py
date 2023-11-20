# Модуль: SUB_QQ_Q
# Автор: Комосский_Егор_2381

from computing.rational.Rational import Rational


# Вычитание двух рациональных чисел
def subtract(self: Rational, other: Rational) -> Rational:

    # Инициализация двух чисел на основе переданных в функцию
    num1 = self.copy()
    num2 = other.copy()

    # Вычитание двух чисел
    num2.numerator = num2.numerator.multiply_by_negative_one()

    # Упрощение и возврат нового числа
    return num1.add(num2).simplify()
