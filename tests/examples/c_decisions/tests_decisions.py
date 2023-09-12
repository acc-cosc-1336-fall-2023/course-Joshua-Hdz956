import unittest

from src.examples.c_decisions.decisions import test_config, get_and_result, get_or_result, get_notted_value, is_even, is_odd, is_vowel, is_consonant, is_overtime

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_and_truth_table(self):
        self.assertEqual(True, get_and_result(True, True))
        self.assertEqual(False, get_and_result(True, False))
        self.assertEqual(False, get_and_result(False, True))
        self.assertEqual(False, get_and_result(False, False))

    def test_or_truth_table(self):
        self.assertEqual(True, get_or_result(True, False))
        self.assertEqual(False, get_or_result(False, False))
        self.assertEqual(True, get_or_result(False, True))
        self.assertEqual(True, get_or_result(True, True))
    
    def test_not_truth_table(self):
        self.assertEqual(False, get_notted_value(True))
        self.assertEqual(True, get_notted_value(False))
    
    def test_is_even(self):
        self.assertEqual(True, is_even(2))
        self.assertEqual(False, is_even(3))
        self.assertEqual(True, is_even(100))
        self.assertEqual(False, is_even(101))

    def test_is_odd(self):
        self.assertEqual(False, is_odd(2))
        self.assertEqual(True, is_odd(3))
        self.assertEqual(False, is_odd(100))
        self.assertEqual(True, is_odd(101))

    def test_is_vowel(self):
        self.assertEqual(True, is_vowel('a'))
        self.assertEqual(True, is_vowel('e'))
        self.assertEqual(True, is_vowel('i'))
        self.assertEqual(True, is_vowel('o'))
        self.assertEqual(True, is_vowel('u'))

    def test_is_consonant(self):
        self.assertEqual(True, is_consonant('g'))
        self.assertEqual(False, is_consonant('e'))

    def test_is_overtime(self):
        self.assertEqual(False, is_overtime(30))
        self.assertEqual(True, is_overtime(41))