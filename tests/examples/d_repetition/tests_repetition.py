import unittest

from src.examples.d_repetition.repetition import test_config, display_numbers, sum_of_squares, for_sum_of_squares, get_sum, get_sum_for

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares(3), 14)
        self.assertEqual(sum_of_squares(2), 5)
        self.assertEqual(sum_of_squares(4), 30)
        self.assertEqual(sum_of_squares(5), 55)

    def test_for_sum_of_squares(self):
        self.assertEqual(for_sum_of_squares(3), 14)
        self.assertEqual(for_sum_of_squares(5), 55)
        self.assertEqual(for_sum_of_squares(4), 30)
        self.assertEqual(for_sum_of_squares(2), 5)

    def test_get_sum_while(self):
        self.assertEqual(get_sum(3), 6)
        self.assertEqual(get_sum(4), 10)
        self.assertEqual(get_sum(5), 15)
        self.assertEqual(get_sum(6), 21)
        self.assertEqual(get_sum(7), 28)
    
    def test_get_sum_for(self):
        self.assertEqual(get_sum_for(3), 6)
        self.assertEqual(get_sum_for(4), 10)
        self.assertEqual(get_sum_for(5), 15)
        self.assertEqual(get_sum_for(6), 21)
        self.assertEqual(get_sum_for(7), 28)
