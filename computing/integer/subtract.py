# Модуль: SUB_ZZ_Z
# Автор: Комосский_Егор_2381

from .Integer import Integer

# Вычитание из первого числа второго
def subtract(num1: Integer, num2: Integer) -> Integer:
    # Вызываем функцию сложения чисел, но меняем знак у второго числа
    return num1.add(num2.multiply_by_negative_one())
