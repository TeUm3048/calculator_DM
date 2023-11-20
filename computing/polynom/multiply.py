# Модуль: MUL_PP_P
# Автор: Потапова_Дарья_2381


from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational


# Умножение многочленов
def multiply(poly1: Polynom, poly2: Polynom) -> Polynom:

    # Создание многочлена, в который будет записываться результат умножения
    result = Polynom([Rational("0")])

    # Создание копий первого и второго многочленов для дальнейшей работы
    pol1 = poly1.copy()
    pol2 = poly2.copy()

    # Последовательный обход второго многочлена
    for i in range(pol2.get_degree() + 1):

        # added - временное слагаемое, полученное путем умножения первого многочлена на одночлен степени i
        added = pol1.multiply_by_monomial(i)

        # Добавление к результату полученного слагаемого, умноженного на коэффициент, соответствующий степени i
        result = result.add(added.multiply_by_scalar(pol2.data[i]))
    return result


