# Автор: Богатов_Илья_2381

from .Polynom import Polynom


def get_leading_coefficient(self: Polynom):
    if len(self.data) > 0:
        return self.data[-1]
    else:
        return None
