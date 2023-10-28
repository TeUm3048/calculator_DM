# Модуль: MUL_ND_N
# Автор: Кривов_Савелий_2381

from .Natural import Natural


def multiply_by_power_of_10(num: Natural, k: Natural) -> Natural:
    number = num.copy()
    times = sum(d * (10 ** i) for i, d in enumerate(k.data))
    for i in range(times):
        number.data.insert(0, 0)
    return number
