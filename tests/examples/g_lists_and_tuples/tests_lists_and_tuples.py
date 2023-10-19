import unittest

from src.examples.g_lists_and_tuples.lists import get_list_total_for, get_list_total_while, list_ref_parameter,get_list_return_value, search_for_item_in_list

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

    def test_list_slicing_start_end(self):
        days = ['Sun','Mon','Tues','Wed','Thurs','Fri','Sat']
        self.assertEqual(days[2:5], ['Tues','Wed','Thurs'])

    def test_list_slicing_start_no_end(self):
        list = [1,2,3,4,5]
        self.assertEqual(list[2:],[3,4,5])

    def test_list_slicing_w_step(self):
        list = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(list[1:8:2], [2,4,6,8])
    
    def test_list_slicing_start_from_end(self):
        list = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(list[-5:], [6,7,8,9,10])

    def test_item_in_list(self):
        nums = ['475','298','894','ABD']
        self.assertEqual(search_for_item_in_list('475', nums), True)
        self.assertEqual(search_for_item_in_list('999', nums), False)

    def test_list_copy_doesnt_create_another_list(self):
        list1 = [1,2,3,4]
        list2 = list1
        list2[0] = 0
        self.assertEqual(list1,list2)
        self.assertEqual(id(list1),id(list2))
    
    def test_variable_copy_does_create_another_list(self):
        num1 = 3
        num2 = 3
        self.assertEqual(num1,3)
        self.assertEqual(num2,3)
        print(id(num1))
        print(id(num2))
        self.assertEqual(id(num1) != id(num2), False)

    def test__create_list_from_existing_lists(self):
        list1 = [1,2,3,4]
        list2 = []

        for i in range(0 , len(list1)):
            list2.append(list1[i])

        self.assertEqual(list1 == list2, True)

        list1[0] = 0

        self.assertEqual(list1 == list2, False)
        self.assertEqual(list1[0] == list2[0], False)
        self.assertEqual(list1[0] == 0, True)
        self.assertEqual(list2[0] == 1, True)

    def test_create_list_from_existing_list_conc(self):
        list1 = [1,2,3,4]
        list2 = [] + [1,2,3,4]
        list1[0] = 0
        self.assertEqual(list1 == list2, False)
        self.assertEqual(list1[0] == list2[0], False)
        self.assertEqual(list1[0] == 0, True)
        self.assertEqual(list2[0] == 1, True)

    def test_list_find_item_at_index(self):
        list1 = [1,2,3,4]

        self.assertEqual(list1.index(2), 1)
        self.assertEqual(list1.index(3), 2)
        self.assertEqual(list1.index(1), 0)

    def test_insert_index(self):
        list1 = [1,2,3,4]
        list1.insert(2,5)
        self.assertEqual(list1, [1,2,5,3,4])

    def test_delete_at_index(self):
        list = [1,2,3,4,5,6,7,8,9,10]
        del list[2]
        self.assertEqual(list, [1,2,4,5,6,7,8,9,10])

    def test_get_max_list(self):
        list = [2,1,3,4,5,6,7,8,9,10]
        self.assertEqual(max(list),10)
        self.assertEqual(min(list),1)

    