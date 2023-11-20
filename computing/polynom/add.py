# Модуль: ADD_PP_P
# Автор: Кривов_Савелий_2381

from computing.polynom.Polynom import Polynom

# Сложение многочленов
def add(self: Polynom, other: Polynom) -> Polynom:

# Создание копий первого и второго многочленов для дальнейшей работы
    num1 = self.copy()
    num2 = other.copy()

# Сохранение длины многочлена меньшей степени
    min_len = min(len(num1.data), len(num2.data))

# Сложение коэффициентов при соответствующих степенях до конца многочлена меньшей степени
    res = [num1.data[i].add(num2.data[i]) for i in range(min_len)]

# Запись в результат оставшихся коэффициентов многочлена большей степени
    if len(num1.data) > min_len:
        res.extend(num1.data[min_len:])
    elif len(num2.data) > min_len:
        res.extend(num2.data[min_len:])

# Возврат нового многочлена
    return Polynom(res)
