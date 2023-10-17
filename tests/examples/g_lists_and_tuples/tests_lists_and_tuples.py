import unittest

from src.examples.g_lists_and_tuples.lists import get_list_total_for, get_list_total_while, list_ref_parameter,get_list_return_value

class Test_Config(unittest.TestCase):

    def test_get_total_w_while(self):
        list1 = [5,10,20]
        self.assertEqual(get_list_total_while(list1), 35)

    def test_get_total_w_for(self):
        list1 = [5,10,20]
        self.assertEqual(get_list_total_for(list1), 35)

    def test_list_param_not_a_copy(self):
        list1 = [5,10,20]
        list_ref_parameter(list1)
        print(list1)
        print(id(list1))
        self.assertEqual(list1, [0,10,20])

    def test_list_return_value(self):
        list1 = [5,10,20]
        print(id(list1))
        get_list_return_value(list1)
        print(id(list1))
        self.assertEqual(list1, [0,10,20])