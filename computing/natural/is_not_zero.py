# Модуль: NZER_N_B
# Автор: Ваньков_Ярослав_2382

from .Natural import Natural

# Проверка числа на неравенство нулю (Эквивалентно != Natural("0"))
def is_not_zero(num: Natural) -> bool:
    # Если длина равна 1, а первая цифра - 0, то это ноль
    # В противном случае возвращаем True
    return not (len(num) == 1 and num.data[0] == 0)
