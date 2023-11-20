# Модуль: MUL_ND_N
# Автор: Богатов_Илья_2381

from .Natural import Natural
from .Natural import Digit

# Умножение на цифру
def multiply_by_digit(num: Natural, digit: Digit) -> Natural:

    # Обработка тривиального случая digit = 0
    if digit == 0:
        return Natural('0')

    # carry - "В уме", то что переносится на следующие разряды
    # result - Массив цифр итогово ответа
    carry, result = 0, []
    
    # Последовательная обработка разрядов
    for d in num.data:
        
        # total - результат умножения текущей цифры, с учётом переноса
        total = d * digit + carry
        
        # Запись последней цифры произведения в ответ
        result.append(total % 10)
        
        # Пересчёт переносимой части произведения
        carry = total // 10
    
    # Добавление разряда при необходимости
    if carry > 0:
        result.append(carry)

    # Создание и возврат нового числа на основе массива цифр
    return Natural(''.join(map(str, result[::-1])))