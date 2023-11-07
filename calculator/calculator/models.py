from computing.natural.Natural import Natural
from computing.integer.Integer import Integer


class NaturalModel:
    def __init__(self, num: Natural):
        self.type = "natural"
        self.num = str(num)


class IntegerModel:
    def __init__(self, num: Integer):
        self.type = "natural"
        self.num = str(num)


num1 = NaturalModel(Natural("6"))
