# Модуль: MUL_NN_N
# Автор: Вакуленко_Инна_2382

from .Natural import Natural

# Уможение чисел
def multiply(num1: Natural, num2: Natural) -> Natural:
    res = Natural("0")

    # Цикл по длине второго числа (умножение в столбик)
    for i in range(len(num2)):
        # Прибавление к результату умножение на цифру с со сдвигом в соотвествующее число разрядов
        res = res.add(num1.multiply_by_digit(num2.data[i]).multiply_by_power_of_10(Natural(str(i))))
    return res
