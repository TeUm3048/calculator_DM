# Автор: Богатов_Илья_2381

from .Polynom import Polynom


# Функция получающая старший коэффициент полинома.
def get_leading_coefficient(self: Polynom):
    return self.data[-1]
