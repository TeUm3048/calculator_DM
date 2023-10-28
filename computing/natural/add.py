# Модуль: ADD_NN_N
# Автор: Газукина_Дарья_2381

from .Natural import Natural
from .compare import compare

def add (num1: Natural, num2: Natural) -> Natural:
    increased = num1.copy()
    added = num2.copy()
    if num1.compare(num2) == 2:
        added.data += [0] * (len(num1) - len(num2))
    else:
        increased.data += [0] * (len(num2) - len(num1))

    for i in range(len(increased)):
        increased.data[i] += added.data[i]
        if increased.data[i] > 9:
            increased.data[i] -= 10
            if i + 1 < len(increased):
                increased.data[i + 1] += 1
            else:
                increased.data.append(1)

    while len(increased) > 1 and increased.data[-1] == 0:
        increased.data.pop()

    return increased