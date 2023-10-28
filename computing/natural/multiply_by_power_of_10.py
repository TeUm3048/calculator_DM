# Модуль: MUL_ND_N
# Автор: Кривов_Савелий_2381

from .Natural import Natural
from .subtract import subtract


def multiply_by_power_of_10(num: Natural, k: Natural) -> Natural:
    number = num.copy()
    times = k.copy()
    number.data.reverse()
    while times.compare(Natural(str(0))) != 0:
        number.data.append(0)
        times = subtract(times, Natural(str(1)))
    number.data.reverse()

    return number
