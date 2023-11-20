# Модуль: SUB_NDN_N
# Автор: Потапова_Дарья_2381

from .Natural import Natural, Digit

# Вычитание из числа другого, домноженного на цифру
# в случаях, когда это допустимо в натульных числах
def subtract_product_from_natural(num1: Natural, num2: Natural, k: Digit) -> Natural:
    # Вычисляем вычитаемое через метод умножения на цифру
    subtrahend = num2.multiply_by_digit(k)
    # Вычитаем
    res = num1.subtract(subtrahend)
    return res
