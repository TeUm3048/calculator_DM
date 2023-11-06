from computing.natural.Natural import Natural


class NaturalModel:
    def __init__(self, num: Natural):
        self.type = "natural"
        self.num = str(num)


num1 = NaturalModel(Natural("6"))
