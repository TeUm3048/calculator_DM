from .Polynom import Polynom


# Нахождение степени полинома
def get_degree(self: Polynom):
    # Находим длину списка полиномов и отнимаем 1
    return len(self.data) - 1
