# Модуль: LCM_NN_N
# Автор: Ильясов_Марк_2381

from .Natural import Natural
from gcd import gcd
from multiple import multiple

def lcm(num1: Natural, num2: Natural) -> Natural:
    return (num1.multiply(num2)).div((num1.gcd(num2)))
