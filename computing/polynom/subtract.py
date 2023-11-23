# Модуль: SUB_PP_P
# Автор: Кривов_Савелий_2381

from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational

# Вычитание многочленов
def subtract(self: Polynom, other: Polynom) -> Polynom:

# Создание копий первого и второго многочленов для дальнейшей работы
    num1 = self.copy()
    num2 = other.copy()

# Умножение одного из многочленов на -1 с целью получения противоположного данному многочлена
    num2 = num2.multiply_by_scalar(Rational("-1"))

# Возврат сложения двух многочленов: исходного первого и противоположного второму
    return num1.add(num2)

