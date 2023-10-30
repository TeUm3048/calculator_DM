from .Integer import Integer


def mod(num1: Integer, num2: Integer) -> Integer:
    if not num2.number.is_not_zero():
        raise ZeroDivisionError
    return num1.subtract(num1.div(num2).multiply(num2))
