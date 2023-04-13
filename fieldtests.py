import unittest

from finite_fields.finite_fields_module import get_field, _BaseFiniteField


class MyTestCase(unittest.TestCase):

    # region typechecks etc

    def test_class_equality(self):
        """
        Tests th
        :return:
        """
        F_5: _BaseFiniteField = get_field(5)
        F_5_2: _BaseFiniteField = get_field(5)
        self.assertTrue(F_5.type_equals(F_5_2))
        F_7: _BaseFiniteField = get_field(7)
        self.assertFalse(F_5.type_equals(F_7))

        self.assertFalse(F_5.type_equals(str))

    def test_equality(self):
        """
        Tests the functionality of the equality operator
        Two equal numbers of essentially the same field should be considered equal
        :return:
        """
        F_5 = get_field(5)
        F_5_2 = get_field(5)
        three_m5 = F_5(3)
        three_m5_2 = F_5(3)

        F_7 = get_field(7)
        three_deluxe = F_7(3)
        self.assertEqual(three_m5, three_m5_2, msg="elements in the same field should be considered equal")
        self.assertNotEqual(three_m5, "three")
        self.assertNotEqual(three_m5, three_deluxe)

    # endregion

    # region basic arithmetic

    def test_addition(self):
        F_7 = get_field(7)
        two = F_7(2)
        three = F_7(3)
        five = F_7(5)
        self.assertEqual(two + three, five)
        five_mod11 = get_field(11)(5)

        self.assertRaises(TypeError, lambda: five + five_mod11)

    def test_subtraction(self):
        F_7 = get_field(7)
        F_5 = get_field(5)
        three: F_7 = F_7(3)
        four: F_7 = F_7(4)
        one: F_7 = F_7(1)
        six: F_7 = F_7(6)
        self.assertEqual(four - three, one)
        self.assertEqual(three - four, six)
        self.assertRaises(TypeError, lambda: three - get_field(11)(3))

    def test_negation(self):
        F_5 = get_field(5)
        three: F_5 = F_5(3)
        two: F_5 = F_5(2)
        self.assertEqual(-three, two)

    def test_multiplication(self):
        F_7: type = get_field(7)
        three: F_7 = F_7(3)
        two = F_7(2)
        F_5 = get_field(5)
        two_mod5: F_5 = F_5(2)
        self.assertEqual(three * three, two)
        self.assertRaises(TypeError, lambda: three * two_mod5)

    def test_division(self):
        F_5 = get_field(5)
        F_7 = get_field(7)
        four: F_5 = F_5(4)
        three: F_5 = F_5(3)
        zero: F_5 = F_5(0)
        three_mod7: F_7 = F_7(3)
        self.assertEqual(F_5(1) / three, F_5(2))
        self.assertEqual(four / three, three)
        self.assertRaises(TypeError, lambda: three / three_mod7)
        self.assertRaises(ZeroDivisionError, lambda: three / zero)

    # endregion




if __name__ == '__main__':
    unittest.main()
