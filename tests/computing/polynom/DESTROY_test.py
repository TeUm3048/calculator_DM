from itertools import product

from computing.polynom.Polynom import Polynom
from computing.rational.Rational import Rational
from numpy.polynomial import Polynomial as numpy_polynom

def correct_add(a: Polynom, b: Polynom):
    return a.to_numpy() + b.to_numpy()

def correct_substract(a: Polynom, b: Polynom):
    return a.to_numpy() - b.to_numpy()

def correct_div(a: Polynom, b: Polynom):
    return a.to_numpy() // b.to_numpy()

def correct_mod(a: Polynom, b: Polynom):
    return a.to_numpy() % b.to_numpy()

rationals = [Rational("0"), Rational("3/10"), Rational("-3/10"), Rational("22/100")]
polynoms_for_test = [Polynom(list(coeffs)) for coeffs in product(rationals, repeat=3)]

def old_test_add_default():
    for poly1 in polynoms_for_test:
        for poly2 in polynoms_for_test:
            assert(poly1.add(poly2) == correct_add(poly1, poly2))

def old_test_subtract_default():
    for poly1 in polynoms_for_test:
        for poly2 in polynoms_for_test:
            assert(poly1.subtract(poly2) == correct_substract(poly1, poly2))

def old_test_div_default():
    k = 0
    for poly1 in polynoms_for_test:
        for poly2 in polynoms_for_test:
            if poly2.is_null():
                continue
            k += 1
            #    assert(not poly1.divide(poly2).is_null())
            assert(poly1.divide(poly2) == correct_div(poly1, poly2))

def test_mod_default():
    #k = 0
    for poly1 in polynoms_for_test:
        for poly2 in polynoms_for_test:
            if poly1.is_null() or poly2.is_null():
                continue
            #k += 1
            assert(poly1.mod(poly2) == correct_mod(poly1, poly2))
            #if (k == 00):
            #    assert(False and (f"~{k}/{len(polynoms_for_test)**2}"))
