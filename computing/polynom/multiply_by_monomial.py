# Модуль: MUL_Pxk_P
# Автор: Ильясов_Марк_2381

from typing import Union
from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational
from computing.natural.Natural import Natural

# Умножение на x^k
def multiply_by_monomial(self: Polynom, k: Union[int, Natural]) -> Polynom:

    # Проверка базового случая нулевого многочлена
    if self.is_null():
        return self.copy()

    # Копирование многочлена и разворот массива коеффициентов, для удобного добавления в начало
    result = self.copy()
    result.data.reverse()

    # Обработка в случае, когда тип аргумента int
    if isinstance(k, int):
        # Добавление нулей
        result.data.extend([Rational("0") for i in range(k)])
        # Разворот обратно
        result.data.reverse()
        # Возврат результата
        return result

    power = k.copy()
    one = Natural("1")
    
    # Цикл по значению степени
    while power.is_not_zero():
        # Добавление нуля
        result.data.append(Rational("0"))
        # Уменьшение счётчика (значения степени)
        power = power.subtract(one)
    
    # Разворот обратно
    result.data.reverse()
    # Возврат результата
    return result

# Примечание:
# Параметр k может иметь тип int, так как длинная аримфетика на массивах имеет свои ограчения
# Так, обращение по индексу это операция, связанная с использованием стандартного целочисленного типа
# Поэтому, длина массива ограничена размерами int, а умножение на 10^k увлечивает длину на k,
# значит и k ограничен, по меньшей мере, размером типа данных int.
# В Python это не существенно, однако в других языках стоило бы обратить на это внимание
