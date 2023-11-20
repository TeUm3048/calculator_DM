# Модуль: DER_P_P
# Автор: Газукина_Дарья_2381

from .Polynom import Polynom
from computing.rational.Rational import Rational

# Взятие производной многочлена
def derive(pol: Polynom) -> Polynom:
    # Создание копии многочлена, чтобы не менять исходный
    derivative = pol.copy()

    # Если на вход подан нулевой многочлен или многочлен, состоящий из одного числа, возвращаем 0 в качестве производной
    if len(derivative.data) <= 1:
        derivative.data[0] = Rational('0')
        return derivative

    # Рассматриваем каждое слагаемое многочлена
    for i in range(len(derivative.data) - 1):
        # Понижаем степень каждого элемента на 1, сдвигая все коэффициенты (элементы data) на один влево
        derivative.data[i] = derivative.data[i + 1]
        # Сознаем индекс/степень degree элемента, следующего за рассматриваемым, с помощью типа Rational
        degree = Rational(str(i + 1))
        # Умножаем коэффициент на degree, получая новый коэффициент
        derivative.data[i] = derivative.data[i].multiply(degree)
    # Удаляем последний элемент нового многочлена, он дублирует предпоследний после сдвига
    derivative.data.pop(-1)

    # Возвращаем многочлен - производную исходного
    return derivative
