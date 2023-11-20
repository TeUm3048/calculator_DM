# Модуль: MOD_PP_P
# Автор: Кузнецов_Илья_2381

from .Integer import Integer

# Остаток от деления числа на число
def mod(num1: Integer, num2: Integer) -> Integer:
    # Проверка на корректность деления
    if not num2.number.is_not_zero():
        raise ZeroDivisionError

    # Возвращаем разность делимого и целой части от деления умноженной на делитель
    return num1.subtract(num1.div(num2).multiply(num2))
