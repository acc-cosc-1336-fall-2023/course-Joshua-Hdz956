import unittest

from src.examples.d_repetition.repetition import test_config, display_numbers, sum_of_squares

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares(3), 14)
        self.assertEqual(sum_of_squares(2), 5)
        self.assertEqual(sum_of_squares(4), 30)
        self.assertEqual(sum_of_squares(5), 55)

