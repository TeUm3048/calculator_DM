# Модуль: SUB_NN_N
# Автор: Комосский_Егор_2381

from .Natural import Natural

# Вычитание натуральных чисел
def subtract(self: Natural, other: Natural) -> Natural:
    
    # Копирование для дальнейшей обработки
    num1 = self.copy()
    num2 = other.copy()
    
    # Вычитание из меньшего больше не допускается
    if num1.compare(num2) == 1:
        raise ValueError
    
    # Цикл по разрядам вычитаемого, вычитание в столбик
    for i in range(len(num2)):
        
        # Находим разность цифр
        num1.data[i] = num1.data[i] - num2.data[i]
        
        j = i
        # Если в результате вычитания цифр получилось отрицательное, "занимаем"
        # из следующего разряда. Если при занимании из следующего разряда получилось отрицательное, повторяем
        while num1.data[j] < 0:
            num1.data[j] += 10
            num1.data[j + 1] -= 1
            j += 1
    
    # Удаление ведущих нулей, которые могли образоваться
    while num1.data[-1] == 0 and len(num1) != 1:
        num1.data.pop()
    return num1
