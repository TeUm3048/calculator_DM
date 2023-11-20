# Модуль: ADD_NN_N
# Автор: Газукина_Дарья_2381

from .Natural import Natural

# Сложение натуральных чисел
def add (num1: Natural, num2: Natural) -> Natural:
    # Создаем копии натуральных чисел: в зависимости от их длины записываем в разные переменные типа Natural
    increased = num1.copy() if (len(num1) > len(num2)) else num2.copy()
    added = num2.copy() if (len(num1) > len(num2)) else num1.copy()
    # Получаем бОльшую длину из длин чисел
    max_len = max(len(num1), len(num2))

    for i in range(max_len):
        # Если не дошли до конца числа, которое прибавляем,
        # складываем цифры, стоящие на одном разряде
        if i < len(added):
            increased.data[i] += added.data[i]

        # Если результат сложения оказался больше 9
        if increased.data[i] > 9:
            # Вычитаем из результата сложения 10
            increased.data[i] -= 10

            # Если не дошли до конца массива увеличиваемого числа,
            # прибавляем к следующему разряду единицу
            if i + 1 < len(increased):
                increased.data[i + 1] += 1
            # Иначе добавляем к массиву числа новый элемент - единицу
            else:
                increased.data.append(1)

    # Возвращаем результат сложения - новое натуральное число
    return increased
