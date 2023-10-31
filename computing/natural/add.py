# Модуль: ADD_NN_N
# Автор: Газукина_Дарья_2381

from .Natural import Natural

def add (num1: Natural, num2: Natural) -> Natural:
    increased = num1.copy() if (len(num1) > len(num2)) else num2.copy()
    added = num2.copy() if (len(num1) > len(num2)) else num1.copy()
    max_len = max(len(num1), len(num2))

    for i in range(max_len):
        if i < len(added):
            increased.data[i] += added.data[i]
        if increased.data[i] > 9:
            increased.data[i] -= 10
            if i + 1 < len(increased):
                increased.data[i + 1] += 1
            else:
                increased.data.append(1)

    return increased
