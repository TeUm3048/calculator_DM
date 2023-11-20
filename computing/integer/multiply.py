from .Integer import Integer, Natural

# Умножение двух целых чисел
def multiply(num1: Integer, num2: Integer) -> Integer:
    # Реализуется умножение в столбик
    # Результат умножения по умолчанию равен 0
    res = Integer("0")
    # Цикл по разрядам num2
    for i in range(len(num2)):
        # Прибавление к модулю результата очередной цифры домноженной на второе число и соответсвующую степень 10
        res.number = res.number.add(num1.number.multiply_by_digit(
            num2.number.data[i]).multiply_by_power_of_10(Natural(str(i))))
    # Определяется знак итогового числа, равный произведению знаков множителей
    res.sign = num1.sign * num2.sign
    return res
