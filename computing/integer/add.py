# Модуль: ADD_ZZ_Z
# Автор: Комосский_Егор_2381

from .Integer import Integer


def add(self: Integer, other: Integer) -> Integer:
    num1 = self.copy()
    num2 = other.copy()
    if num1.determinate_sign() == num2.determinate_sign():
        num1.number = num1.number.add(num2.number)
        return num1
    match num1.number.compare(num2.number):
        case 2:
            num1.number = num1.number.subtract(num2.number)
            return num1
        case 1:
            num2.number = num2.number.subtract(num1.number)
            return num2
        case 0:
            return Integer('0')




