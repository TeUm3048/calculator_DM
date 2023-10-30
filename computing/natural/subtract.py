# Модуль: SUB_NN_N
# Автор: Комосский_Егор_2381

from .Natural import Natural


def subtract(self: Natural, other: Natural) -> Natural:
    num1 = self.copy()
    num2 = other.copy()
    if num1.compare(num2) == 1:
        raise ValueError
    for i in range(len(num2)):
        num1.data[i] = num1.data[i] - num2.data[i]
        j = i
        while num1.data[j] < 0:
            num1.data[j] += 10
            num1.data[j + 1] -= 1
            j += 1
    while num1.data[-1] == 0 and len(num1) != 1:
        num1.data.pop()
    return num1
