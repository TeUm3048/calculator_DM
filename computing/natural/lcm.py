# Модуль: LCM_NN_N
# Автор: Ильясов_Марк_2381

from .Natural import Natural

# Наименьшее общее кратное
def lcm(num1: Natural, num2: Natural) -> Natural:
    # Вычисляется по формуле НОК(a, b) = a * b / НОД(a, b)
    return (num1.multiply(num2)).div((num1.gcd(num2)))