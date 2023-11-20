# Модуль: DIV_NN_N
# Автор: Рыжиков_Иван_2381

from .Natural import Natural


def div(num1: Natural, num2: Natural) -> Natural:
    # Не допускается деление на ноль
    if not num2:
        raise ZeroDivisionError

    # Копирование исходных чисел для дальнейшей работы
    a = num1.copy()
    b = num2.copy()

    res = Natural("0")

    # Алгоритм деления в столбик
    while a >= b:
        # Получаем первую цифру частного (домноженную на соответсвующую степень 10)
        digit_with_zeros = a.get_digit_of_division_with_power(b)
        # Вычитаем из делимого полученное значение, домноженное на делитель
        a -= digit_with_zeros * b
        # Увеличиваем результат
        res += digit_with_zeros
    return res
