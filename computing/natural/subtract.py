# Модуль: SUB_NN_N
# Автор: Комосский_Егор_2381

from Natural import Natural


def subtract(num1: Natural, num2: Natural) -> Natural:
    if num1 < num2:
        num1, num2 = num2, num1
    for i in range(len(num2)):
        num1.data[i] = num1.data[i] - num2.data[i]
        if num1.data[i] < 0:
            num1.data[i] += 10
            num1.data[i+1] -= 1
    if num1.data[-1] == 0:
        while num1.data[-1] == 0:
            num1.data.pop()
    return num1

