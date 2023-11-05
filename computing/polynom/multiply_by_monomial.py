# Модуль: 

from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational
from computing.natural.Natural import Natural


def multiply_by_monomial(self: Polynom, k: int) -> Polynom:
    result = self.copy()
    result.data = [Polynom(Rational("0")) for i in range(k)] + result.data
    return result

# я отказываюсь так плохо писать
# я безумно опечален, что такой код может существовать в мире
# я думал, что хуже быть уже быть не может
# мне сложно это больше терпеть
# меня заставили
# простите все кто считает себя программистом
# прошу, уберите от экрана детей и беременных жещнин
# будь моя воля этого бы всего не было
def very_bad_multiply_by_monomial(self: Polynom, k: Natural) -> Polynom:
    oh_cringe = Polynom.copy()
    sorry_for_this = k.copy()
    i_was_forced = Natural("1")
    while k.is_not_zero():
        oh_cringe.data = [Natural("0")] + oh_cringe.data
        sorry_for_this.subtract(i_was_forced)
    return oh_cringe
