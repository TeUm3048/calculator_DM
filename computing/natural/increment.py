# Модуль: ADD_1N_N
# Автор: Кривов_Савелий_2381

from .Natural import Natural

# Инкримент, увленичение числа на 1
# Одна из немногих функций, которая изменяет число непосредственно
def increment(self: Natural) -> None:
    self.data[0] += 1
    # Цикл в случае переполнения разряда
    if self.data[0] > 9:
        for i in range(0, len(self.data) - 1):
            if self.data[i] > 9:
                self.data[i] = 0
                self.data[i + 1] += 1
    # Добавление разряда при необходимости
    if self.data[-1] > 9:
        self.data[-1] = 0
        self.data.append(1)
