# Модуль: LCM_NN_N
# Автор: Ильясов Марк 2381

from Natural import Natural


def lcm(num1: Natural, num2: Natural) -> Natural:
    return num1 * num2 // (num1 % num2)