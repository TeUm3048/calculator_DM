# Модуль: ADD_ZZ_Z
# Автор: Комосский_Егор_2381

from .Integer import Integer

# Сложение двух чисел
def add(self: Integer, other: Integer) -> Integer:
    num1 = self.copy()
    num2 = other.copy()
    # Сравнение знаков у чисел
    if num1.determinate_sign() == num2.determinate_sign():
        # Если знаки одинаковые, то складываем абсолютные значения и возвращаем сумму с изначальным знаком
        num1.number = num1.number.add(num2.number)
        return num1
    # Если знаки не равны, то сравниваем абсолютные значения
    match num1.number.compare(num2.number):
        case 2:
            # Если первое абсолютное значение первого числа больше, чем абс. значение второго,
            # то вычитаем из первого второе и возвращаем со знаком первого числа
            num1.number = num1.number.subtract(num2.number)
            return num1
        case 1:
            # Если второе больше первого, то вычитаем из второго первое и возвращаем со знаком второго числа
            num2.number = num2.number.subtract(num1.number)
            return num2
        case 0:
            # Если абсолютные значения равны, то возвращаем 0
            return Integer('0')




