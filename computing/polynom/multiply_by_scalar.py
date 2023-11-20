# Модуль: MOD_PP_P
# Автор: Ваньков_Ярослав_2381

from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational

# Умножение на скаляр
def multiply_by_scalar(pol1: Polynom, scalar: Rational) -> Polynom:
    
    # Копирование исходных чисел для дальнейшей работы
    pol = pol1.copy()
    
    # Цикл, в котором каждый итерируемый коэффициент умножается на скаляр
    for i in range(len(pol)):
        pol.data[i] = pol.data[i].multiply(scalar)

    return pol
