# Модуль: MUL_NN_N
# Автор: Вакуленко_Инна_2382

from .Natural import Natural
# from .multiply_by_digit import multiply_by_digit
# from .multiply_by_power_of_10 import multiply_by_power_of_10
# from .add import add


def multiply(num1: Natural, num2: Natural) -> Natural:
    res = Natural("0")
    for i in range(len(num2)):
        res = res.add(num1.multiply_by_digit(num2.data[i]).multiply_by_power_of_10(i))
        # res = add(multiply_by_power_of_10(multiply_by_digit(num1, num2.data[i]), Natural(str(i))), res)
    return res

