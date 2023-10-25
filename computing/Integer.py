from typing import Literal

from Natural import Natural

Sign = Literal[-1, 1, 0]


class Integer:
    data: Natural
    sign: Sign
    pass
