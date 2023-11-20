# Модуль: ADD_NN_N
# Автор: Газукина_Дарья_2381

from .Natural import Natural

# Сложение двух натуральных чисел
def add (num1: Natural, num2: Natural) -> Natural:
    # в increased сохраняем копию числа с наибольшей длиной,
    # в added - оставшееся число
    increased = num1.copy() if (len(num1) > len(num2)) else num2.copy()
    added = num2.copy() if (len(num1) > len(num2)) else num1.copy()

    # сохраняем максимальную длину
    max_len = max(len(num1), len(num2))

    # пробегаем поразрядным циклом
    for i in range(max_len):

        # складываем соответсвующие разряды, пока счётчик не превышает длину обоих чисел 
        if i < len(added):
            increased.data[i] += added.data[i]
        
        # осуществляем перенос на следующий разряд в случае переполнения
        if increased.data[i] > 9:
            increased.data[i] -= 10
            
            # создаём разряд при необходимости
            if i + 1 < len(increased):
                increased.data[i + 1] += 1
            else:
                increased.data.append(1)

    return increased

