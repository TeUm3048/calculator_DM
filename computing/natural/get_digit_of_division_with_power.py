# Модуль: DIV_NN_Dk
# Автор: Мавликаев_Иван_2381

from .Natural import Natural
from .Natural import Digit

# Возвращает первую цифру от деления, домноженную на соотвествующую степень 10
# Например, get_digit_of_division_with_power(234, 2) == 100.
# Другие примеры можно увидеть в tests/natural/get_digit_of_division_with_power_test.py
def get_digit_of_division_with_power(num1: Natural, num2: Natural) -> Digit:
    
    # Не допускается деление на ноль
    if not num2.is_not_zero():
        raise ZeroDivisionError
    
    a = num1.copy()
    b = num2.copy()
    
    # Укорачиваем делимое по делителю
    # Равносильно тому, как при делении в столбик ставится штрих, для отделения первых нескольких разрядов
    a.data = a.data[-len(b):]
    
    # Если при таком укорачивании делитель больше, добавляем разряд
    if a < b:
        a.data = num1.data[-len(b) - 1:]
    
    # Записываем число для хранения разрядов
    k = Natural(str(len(num1) - len(a)))
    
    # Вычитаем пока можем, с увеличением ответа
    count = Natural("0")
    while a >= b:
        a -= b
        count += Natural("1")
    
    # Возрат цифры с соотвествующим домножением на степень 10
    return count.multiply_by_power_of_10(k)
