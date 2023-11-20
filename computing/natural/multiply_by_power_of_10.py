# Модуль: MUL_ND_N
# Автор: Кривов_Савелий_2381

from .Natural import Natural


# Умножение на 10^k
def multiply_by_power_of_10(num: Natural, k: Natural) -> Natural:
    
    # Проверка на ноль - его можно не умножать
    if not num.is_not_zero():
        return num
    
    # Создание копии числа для дальнейшей обработки
    number = num.copy()
    # Объявление копии k для цикла
    times = k.copy()
    
    # Разворот числа, для того, чтобы добавление разрядов происходило через append, так быстрее
    number.data.reverse()

    # Цикл до конца счётчика
    while times.is_not_zero():
        # Добавление нулевого разряда
        number.data.append(0)

        # Вычитание единицы из счётчика
        times = times.subtract(Natural('1'))
    
    # Разворот цифр числа обратно
    number.data.reverse()

    # Возврат ответа
    return number
