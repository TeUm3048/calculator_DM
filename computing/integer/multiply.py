from .Integer import Integer, Natural


def multiply(num1: Integer, num2: Integer) -> Integer:
    res = Integer("0")
    for i in range(len(num2)):
        res.number = res.number.add(num1.number.multiply_by_digit(
            num2.number.data[i]).multiply_by_power_of_10(Natural(str(i))))
    res.sign = num1.sign * num2.sign
    return res
