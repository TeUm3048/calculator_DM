# Модуль: MOD_NN_N
# Автор: Кузнецов_Илья_2381

from .Natural import Natural

# Остаток от деления
def mod(num1: Natural, num2: Natural) -> Natural:
    # MOD не определён для второго нулевого значения
    if not num2.is_not_zero():
        raise ZeroDivisionError
    # MOD можно выразить через DIV из формулы  a = mod(a, b) + div(a, b)
    return num1.subtract(num1.div(num2).multiply(num2))
