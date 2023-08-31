import unittest

from src.examples.a_example.devprocess import add_numbers, floating_point_division, echo_number, operator_precedence_1, integer_division, operator_precedence_2, square_value, get_remainder


class Test_Config(unittest.TestCase):

    def test_add_numbers_2(self):
        self.assertEqual(2, add_numbers(1, 1))

    def test_echo_number_5(self):
        self.assertEqual(5, echo_number(5))

    def test_add_numbers_73(self):
        self.assertEqual(73, add_numbers(30, 43))

    def test_echo_number_35(self):
        self.assertEqual(35, echo_number(35))

    def test_floating_point_division_25(self):
        self.assertEqual(25, floating_point_division(125,5))

    def test_integer_division1(self):
        self.assertEqual(4, integer_division(9,2))

    def test_operator_precedence_1(self):
        self.assertEqual(14, operator_precedence_1(12, 6, 3))

    def test_operator_precedence_2(self):
        self.assertEqual(6, operator_precedence_2(12,6,3))

    def test_square_value(self):
        self.assertEqual(4, square_value(2))

    def test_get_remainder(self):
        self.assertEqual(0, get_remainder(4, 4))

    def test_get_remainder_1(self):
        self.assertEqual(1, get_remainder(11, 2))

    def test_add_numbers_45(self):
        self.assertEqual(4.5, add_numbers (2.25, 2.25))

    def test_add_numbers_44(self):
        self.assertEqual(4.25, add_numbers (2, 2.25))