# Модуль: SUB_ZZ_Z
# Автор: Комосский_Егор_2381

from .Integer import Integer


def subtract(num1: Integer, num2: Integer) -> Integer:
    return num1.add(num2.multiply_by_negative_one())
