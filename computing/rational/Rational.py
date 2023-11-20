from __future__ import annotations
from typing import Literal
from computing.natural.Natural import Natural
from computing.integer.Integer import Integer


class Rational:

    # Создание числителя и знаменателя рационального числа
    numerator: Integer
    denominator: Natural

    # Конструктор класса для рациональных чисел
    def __init__(self, value: str | list[Integer, Natural]) -> None:

        # Проверка, является ли параметр value строкой
        if isinstance(value, str):

            # Разделение строки на числитель и знаменатель по символу '/'
            value = value.split('/')

            # Проверка, состоит ли строка только из числителя
            if len(value) == 1:

                # Если знаменатель не указан, устанавливаем его в 1
                self.numerator = Integer(value[0])
                self.denominator = Natural('1')
            else:

                # Иначе устанавливаем числитель и знаменатель из строки
                self.numerator = Integer(value[0])
                self.denominator = Natural(value[1])
        else:

            # Если параметр value не является строкой, предполагаем, что это список числителя и знаменателя
            self.numerator = value[0]
            self.denominator = value[1]

        # Проверка на случай деления на ноль (знаменатель не может быть нулевым)
        if self.denominator == Natural('0'):
            raise ZeroDivisionError

    # Преобразование рационального числа во float
    def __float__(self):
        return float(int(self.numerator) / int(self.denominator))

    # Перегрузка оператора умножения (*)
    def __mul__(self, other):
        return self.multiply(other)

    # Перегрузка оператора деления (/)
    def __truediv__(self, other):
        return self.divide(other)

    # Метод для упрощения рационального числа
    def simplify(self: Rational):
        if self.numerator.sign == 0:

            # Если числитель равен нулю, возвращаем новый объект Rational с числителем 0
            return Rational("0")

        # Находим наибольший общий делитель (НОД) числителя и знаменателя
        gcd = self.numerator.number.gcd(self.denominator)

        # Делим числитель и знаменатель на НОД, чтобы упростить рациональное число
        simplified_numerator = self.numerator.div(Integer.from_natural(gcd))
        simplified_denominator = self.denominator.div(gcd)

        # Возвращаем новый объект Rational с упрощенным числителем и знаменателем
        return Rational([simplified_numerator, simplified_denominator])

    # Оператор копирования рационального числа
    def copy(self):
        return Rational(str(self))

    # Метод для представления рационального числа в виде строки
    def __str__(self: Rational):
        return (str(self.numerator) + ('/' + str(self.denominator))
                * (self.denominator != Natural('1')))

    # Метод для представления рационального числа в виде строки при использовании функции repr()
    def __repr__(self):
        return f"Rational({self})"

    # Метод, проверяющий, является ли рациональное число целым
    def is_integer(self: Rational):
        tmp = self.simplify()
        return tmp.denominator == Natural('1')

    # Статический метод для создания рационального числа из целого
    @staticmethod
    def from_integer(int: Integer):
        return Rational(int, Natural('1'))

    # Статический метод для создания целого числа из рационального
    @staticmethod
    def to_integer(rat: Rational):
        num1 = rat.copy().simplify()
        if num1.denominator == Natural('1'):
            return num1.numerator
        return rat  ## под вопросом

    # Перегрузка оператора сложения
    def __add__(self, other: Rational) -> Rational:
        return self.add(other)

    # Перегрузка оператор вычитсниая
    def __sub__(self, other: Rational) -> Rational:
        return self.subtract(other)

    # Метод для сложения двух рациональных чисел
    def add(self: Rational, other: Rational) -> Rational:
        from .add import add
        return add(self, other)

    # Метод для вычитания одного рационального числа из другого
    def subtract(self: Rational, other: Rational) -> Rational:
        from .subtract import subtract
        return subtract(self, other)

    # Метод для умножения двух рациональных чисел
    def multiply(self: Rational, other: Rational) -> Rational:
        from .multiply import multiply
        return multiply(self, other)

    # Метод для деления одного рационального числа на другое
    def divide(self: Rational, other: Rational) -> Rational:
        from .divide import divide
        return divide(self, other)

    # Перегрузка оператора "<" (меньше)
    def __lt__(self, other: Rational) -> bool:
        num1 = self.numerator.multiply(Integer.from_natural(other.denominator))
        num2 = other.numerator.multiply(Integer.from_natural(self.denominator))
        return num1 < num2

    # Перегрузка оператора "==" (равно)
    def __eq__(self, other: Rational) -> bool:
        num1 = self.copy().simplify()
        num2 = other.copy().simplify()
        return num1.numerator == num2.numerator and num1.denominator == num2.denominator

    # Перегрузка оператора "<=" (меньше или равно)
    def __le__(self, other: Rational) -> bool:
        return (self < other) or (self == other)

    # Перегрузка оператора "!=" (не равно)
    def __ne__(self, other: Rational) -> bool:
        return not (self == other)

    # Перегрузка оператора ">" (больше)
    def __gt__(self, other: Rational) -> bool:
        return not (self <= other)

    # Перегрузка оператора ">=" (больше или равно)
    def __ge__(self, other: Rational) -> bool:
        return not (self < other)

