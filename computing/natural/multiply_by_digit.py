# Модуль: MUL_ND_N
# Автор: Богатов_Илья_2381

from .Natural import Natural
from .Natural import Digit


def multiply_by_digit(num: Natural, digit: Digit) -> Natural:
    if digit == 0:
        return Natural('0')
    carry, result = 0, []
    for d in num.data:
        total = d * digit + carry
        result.append(total % 10)
        carry = total // 10
    if carry > 0:
        result.append(carry)
    return Natural(''.join(map(str, result[::-1])))