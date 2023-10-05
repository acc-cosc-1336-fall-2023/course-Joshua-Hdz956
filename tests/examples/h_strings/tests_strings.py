import unittest

from src.examples.h_strings.strings import test_config, concat_strings, slice_string, slice_w_step_value, search_in_string

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_concat_strings(self):
        self.assertEqual(concat_strings("abc","def"), 'abcdef')
    
    def test_slice_string(self):
        self.assertEqual(slice_string("Patty Lynn Smith"), 'Lynn')
    
    def test_slice_w_step_value(self):
        self.assertEqual(slice_w_step_value('ABCDEF'), 'ACE')

    def test_search_in_string(self):
        self.assertEqual(search_in_string('abc', 'abcdef'), True)

    def test_compare_string(self):
        str1 = 'c'
        str2 = 'p'
        self.assertEqual(str1 < str2, True)
    
    def test_is_string_digit(self):
        str1 = '1200'
        self.assertEqual(str1.isdigit(), True)
        self.assertEqual('ab'.isdigit(), False)

    def test_string_is_alpha(self):
        str1 = 'abcdefg'
        self.assertEqual(str1.isalpha(), True)
        self.assertEqual('$%$@'.isalpha(), False)
    
    def test_string_is_upper(self):
        str1 = 'XYZ'
        self.assertEqual(str1.isupper(), True)

    def test_string_to_lower(self):
        str1 = 'AFFFGHE'
        self.assertEqual(str1.lower(), 'afffghe')

    def test_strip_char_from_strings(self):
        str1 = 'eeabcdefegefee'
        self.assertEqual(str1.strip('e'), 'abcdefegef')

    def test_lstrip_char_from_strings(self):
        str1 = 'eeabcdefegefee'
        self.assertEqual(str1.lstrip('e'), 'abcdefegefee')

    def test_replace_from_string(self):
        str1 = 'eeabcdefegefee'
        self.assertEqual(str1.replace('e', ''), 'abcdfgf')

    def test_string_repetition_operator(self):
        str1 = 'w' * 5
        self.assertEqual(str1, "wwwww")

    def test_split_strings(self):
        str1 = 'one two three four'
        str_list = str1.split()
        self.assertEqual(str_list[3], 'four')

    def test_split_strings_tab(self):
        str1 = 'one\ttwo\tthree\tfour'
        str_list = str1.split()
        self.assertEqual(str_list[3], 'four')