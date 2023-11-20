# Модуль: GCF_NN_N
# Автор: Ильясов_Марк_2381

from .Natural import Natural


def gcd(num1: Natural, num2: Natural) -> Natural:
    a = num1.copy()
    b = num2.copy()

    # В контексте модуля натуральных чисел, НОД в котором участвует хотя бы
    # один ноль, не определён. Теоретически можно убрать эту проверку, в таком
    # случае НОД будет расширен для нулевых значений (выдаст максимум из двух чисел)
    if not (a.is_not_zero() and b.is_not_zero()):
        raise ZeroDivisionError

    # Алгоритм Евклида
    while a.is_not_zero() and b.is_not_zero():
        a %= b
        a, b = b, a
    return max(a, b)
