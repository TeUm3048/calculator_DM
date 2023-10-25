from typing import Literal

Digit = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


class Natural:
    data: list[Digit]
    length: int

    def __init__(self, value: str) -> None:
        self.data = []
        self.length = 0
        for digit in value:
            self.data = [int(digit)] + self.data
            self.length += 1
        pass

    def __lt__(self, other: 'Natural') -> bool:
        if self.length > other.length:
            return False
        elif self.length < other.length:
            return True
        else:
            i = self.length - 1
            while i >= 0 and self.data[i] == other.data[i]:
                i -= 1
            if i == -1:
                return False
            else:
                if self.data[i] < other.data[i]:
                    return True
                else:
                    return False

    def __eq__(self, other: 'Natural') -> bool:
        if self.length != other.length:
            return False
        else:
            for i in range(self.length):
                if self.data[i] != other.data[i]:
                    break
            else:
                return True
            return False

    def __le__(self, other: 'Natural') -> bool:
        return (self < other) or (self == other)

    def __ne__(self, other: 'Natural') -> bool:
        return not (self == other)

    def __gt__(self, other: 'Natural') -> bool:
        return not (self <= other)

    def __ge__(self, other: 'Natural') -> bool:
        return not (self < other)

    def comparator(self, other: 'Natural') -> int:
        if self < other:
            return -1
        if self > other:
            return 1
        return 0

    def compare(self, other: 'Natural') -> int:
        if self > other:
            return 2
        if self < other:
            return 1
        return 0

    def is_not_zero(self) -> bool:
        return not (self.length == 1 and self.data[0] == 0)
