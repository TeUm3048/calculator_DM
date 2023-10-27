# Модуль: ADD_1N_N
# Автор: Кривов_Савелий_2381

from .Natural import Natural


def increment(self: Natural) -> Natural:
    num = self.copy()
    num.data[-1] + 1
    if num.data[-1] > 9:
        for i in range(len(num)-1, -1, -1):
            if num.data[i] > 9:
                num.data[i] = 0
                num.data[i-1] += 1

    return num