# Модуль: MOD_PP_P
# Автор: Кузнецов_Илья_2381

from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational

# Остаток от деления одного многочлена на другой
def mod(pol1: Polynom, pol2: Polynom) -> Polynom:
    # Создание копий, для безопасности внутренней структуры входных данных
    num1 = pol1.copy()
    num2 = pol2.copy()

    # Возвращаем разность делимого и целой части от деления умноженной на делитель
    return num1.subtract(num2.multiply(num1.divide(num2)))

