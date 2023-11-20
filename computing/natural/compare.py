# Модуль: COM_NN_D
# Автор: Ярослав_Ваньков_2382

from .Natural import Natural
from typing import Literal

# Сравнение двух чисел
# Основывается на методах класса, перегруженных операторов сравнения __gt__() и __lt__(), см. в файле Natural.py
def compare(self: Natural, other: Natural) -> Literal[0, 1, 2]:
    if self > other:
        return 2
    if self < other:
        return 1
    return 0
