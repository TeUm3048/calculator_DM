# DIV_PP_P
# Автор: Ильясов_Марк_2381

from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational

# Деление многочленов
def divide(self: Polynom, other: Polynom) -> Polynom:
    
    # Деление на нулевой многочлен не определено
    if other.is_null():
        raise ZeroDivisionError
    
    # Деление многочлена меньшей степени на многочлен большей степени даёт нулевой многочлен
    if self.degree() < other.degree() or self.is_null():
        return Polynom([Rational("0")])
    
    # Копирование многочленов и объявление переменной для результата
    a = self.copy()
    b = other.copy()
    result = Polynom([Rational("0")])

    # Цикл деления многочлена в столбик
    while a.degree() >= b.degree() and not a.is_null():

        # Опеределяем отношение старших коеффициентов
        coefficient = a[-1] / b[-1]
        
        # Прибавляем к результату одночлен
        # Старший коеффициент которого равен - coefficient, а степень - разности степеней делимого и делителя
        result = result.add(Polynom([coefficient]).multiply_by_monomial(a.degree() - b.degree()))
        
        # Вычитаем из делимого одночлен, домноженный на делимое
        a = a.subtract(b.multiply_by_monomial(a.degree() - b.degree()).multiply_by_scalar(coefficient))

    # Возвращаем результат
    return result
