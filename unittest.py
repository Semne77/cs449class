

import unittest
#from fractions import Fraction

class Fraction:
    def __init__(self, top, bottom):
        if not isinstance(top, int) or not isinstance(bottom, int):
            raise ValueError("Invalid type passed to Fraction constructor")
        
        common_denominator = gcd(top, bottom)
        self.num = top // common_denominator
        self.den = bottom // common_denominator

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, fraction2):
        new_num = self.num * fraction2.den + fraction2.num * self.den
        new_den = self.den * fraction2.den
        return Fraction(new_num, new_den)

    def __sub__(self, fraction2):
        new_num = self.num * fraction2.den - fraction2.num * self.den
        new_den = self.den * fraction2.den
        return Fraction(new_num, new_den)

    def __mul__(self, fraction2):
        new_num = self.num * fraction2.num
        new_den = self.den * fraction2.den
        return Fraction(new_num, new_den)

    def __truediv__(self, fraction2):
        new_num = self.num * fraction2.den
        new_den = self.den * fraction2.num
        return Fraction(new_num, new_den)

    def __eq__(self, fraction2):
        first_num = self.num * fraction2.den
        second_num = fraction2.num * self.den
        return first_num == second_num

    def __gt__(self, fraction2):
        first_num = self.num * fraction2.den
        second_num = fraction2.num * self.den
        return first_num > second_num

    def __ge__(self, fraction2):
        first_num = self.num * fraction2.den
        second_num = fraction2.num * self.den
        return first_num >= second_num

    def __lt__(self, fraction2):
        first_num = self.num * fraction2.den
        second_num = fraction2.num * self.den
        return first_num < second_num

    def __le__(self, fraction2):
        first_num = self.num * fraction2.den
        second_num = fraction2.num * self.den
        return first_num <= second_num

    def __ne__(self, fraction2):
        first_num = self.num * fraction2.den
        second_num = fraction2.num * self.den
        return first_num != second_num

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

def gcd(int1, int2):  # Euclid's algorithm
    while int1 % int2 != 0:
        old_int1 = int1
        old_int2 = int2
        int1 = old_int2
        int2 = old_int1 % old_int2
    return int2


class TestFraction(unittest.TestCase):
    def test_constructor(self):
        with self.assertRaises(ValueError):
            Fraction("abc", 2)#ValueError is raised when a string value is passed as a numerator or denominator.
            Fraction('abs', "def")#not integer passed
            Fraction(5, 1.2)#not integer passed

        with self.assertRaises(ZeroDivisionError):#can not divide by 0
            Fraction(2,0)

        with self.assertRaises(NameError):#NameError is raised when an undefined variable is passed as a parameter.
            Fraction(Four, 8)
            Fraction(eight)
            Fracion(5, 7)#t is missing
        with self.assertRaises(TypeError):#TypeError is raised when only one parameter is passed.
            Fraction(8)# only one parameter


    def test_str(self):
        self.assertEqual(str(Fraction(4, 5)), "4/5")#Asserts that the string representation of a
        # fraction is correctly returned as "numerator/denominator".
        self.assertEqual(str(Fraction(-4, -5)), "4/5")
        self.assertEqual(str(Fraction(-4, 2)), "-2/1")#Asserts that the string representation of
        # a negative fraction is correctly returned with the negative sign before the numerator.
        self.assertEqual(str(Fraction(0,1)), "0/1")
        self.assertEqual(str(Fraction(-0, 1)), "0/1")#checks that -0 = 0

    def test_add(self):
        self.assertEqual(Fraction(1, 2) + Fraction(1, 3), Fraction(5, 6))
        self.assertEqual(Fraction(1, 2) + Fraction(0, 3), Fraction(1, 2))# adding a fraction with zero as its
        # numerator not results in the other fraction.
        self.assertEqual(Fraction(-1, 2) + Fraction(1, 2), Fraction(0, 1))
        self.assertEqual(Fraction(23, 1) + Fraction(11, 1), Fraction(34, 1))#large numbers

    def test_sub(self):
        self.assertEqual(Fraction(3, 4) - Fraction(1, 2), Fraction(1, 4))
        self.assertEqual(Fraction(1, 2) - Fraction(0, 3), Fraction(1, 2))#substracion of 0
        self.assertEqual(Fraction(-1, 2) - Fraction(1, 2), Fraction(1, -1))
    def test_mul(self):
        self.assertEqual(Fraction(2, 3) * Fraction(3, 4), Fraction(1, 2))#Asserts that two fractions can be
        # multiplied correctly.
        self.assertEqual(Fraction(0, 3) * Fraction(3, 4), Fraction(0, 1))#Asserts that multiplying a fraction with
        # zero as its numerator results in zero.
        self.assertEqual(Fraction(2, 3) * Fraction(-3, 4), Fraction(-1, 2))#Asserts that multiplying a negative
        # fraction with a positive fraction produces the negative result.

    def test_div(self):
        self.assertEqual(Fraction(2, 3) / Fraction(4, 5), Fraction(5, 6))
        with self.assertRaises(ZeroDivisionError):#Asserts that dividing a fraction by a zero fraction results in
            # a ZeroDivisionError.
            Fraction(2, 3) / Fraction(0, 5)
        self.assertEqual(Fraction(2, 3) / Fraction(4, -5), Fraction(-5, 6))#Asserts that dividing a fraction by a
        # negative fraction produces the correct result.

    def test_eq(self):
        self.assertTrue(Fraction(1, 2) == Fraction(2, 4))
        self.assertTrue(Fraction(1, 2) != Fraction(-2, 4))#Asserts that two fractions with opposite signs are not
        # equal.
        self.assertTrue(Fraction(1, 2) != Fraction(4, 2))#Asserts that two fractions with different numerators and
        # denominators are not equal.
        self.assertTrue(Fraction(0, 2) == Fraction(0, 4))#Asserts that two zero fractions with different
        # denominators are equal.

    def test_gt(self):
        self.assertTrue(Fraction(3, 4) > Fraction(1, 2))
        self.assertTrue(Fraction(3, 4) > Fraction(-1, 1))#Asserts that a positive fraction is greater than a negative
        # fraction.


    def test_ge(self):
        self.assertTrue(Fraction(3, 4) >= Fraction(3, 4))
        self.assertTrue(Fraction(3, 4) >= Fraction(-4, 4))
        self.assertTrue(Fraction(0, 4) >= Fraction(3, -4))#Asserts that a zero fraction is greater than or equal
        # to a negative fraction.


    def test_lt(self):
        self.assertTrue(Fraction(1, 4) < Fraction(1, 2))
        self.assertTrue(Fraction(-1, 1) < Fraction(1, 2))#Asserts that a negative fraction is less than a
        # positive fraction.

    def test_le(self):
        self.assertTrue(Fraction(1, 2) <= Fraction(1, 2))
        self.assertTrue(Fraction(0, 2) <= Fraction(0, 7))#Asserts that a zero fraction is less than or equal to
        # another
        # zero fraction.

    def test_ne(self):
        self.assertTrue(Fraction(2, 3) != Fraction(3, 4))
        self.assertTrue(Fraction(-2, 3) != Fraction(2, 3))#Asserts that two fractions with opposite signs are not
        # equal.

    def test_getNum(self):
        self.assertEqual(Fraction(2, 3).getNum(), 2)
        self.assertEqual(Fraction(0, 3).getNum(), 0)#Asserts that the numerator of a zero fraction is returned
        # correctly.
        with self.assertRaises(AttributeError):
            Fraction(0, 3).num.getNum()# if object has no attribute 'getNum'


    def test_getDen(self):
        self.assertEqual(Fraction(2, 3).getDen(), 3)#Asserts that the denominator of a fraction is returned correctly.
        with self.assertRaises(AttributeError):
            Fraction(0, 3).num.getDen()# if object has no attribute 'getDen'





if __name__ == '__main__':
    unittest.main()