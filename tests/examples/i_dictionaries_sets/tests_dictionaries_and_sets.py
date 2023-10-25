import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config, is_key_in_dictionary, add_friend_phonebook, update_friend_phonebook, delete_friend_phonebook

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_is_key_in_dictionary(self):
        phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanna':'555-3333'}
        self.assertEqual(is_key_in_dictionary("Chris", phonebook), True)
        self.assertEqual(is_key_in_dictionary("Chrs", phonebook), False)
    
    def test_add_friend_phonebook(self):
        phonebook = {}
        add_friend_phonebook('Cait', '361-4444',phonebook)
        self.assertEqual(len(phonebook),1)
        self.assertEqual(phonebook, {'Cait':'361-4444'})
    
    def test_update_phonebook(self):
        phonebook = {'Josh':'956-444-1111'}
        update_friend_phonebook('Josh','956-564-2716',phonebook)
        self.assertEqual(phonebook, {'Josh':'956-564-2716'})
        update_friend_phonebook('Joshh','956-564-2716',phonebook)
        self.assertEqual(phonebook, {'Josh':'956-564-2716'})
    
    def test_delete_from_phonebook(self):
        phonebook = {}
        add_friend_phonebook('Josh','956-333-1111',phonebook)
        add_friend_phonebook('Joshh','956-333-2222',phonebook)
        self.assertEqual(phonebook, {'Josh':'956-333-1111','Joshh':'956-333-2222'})
        delete_friend_phonebook('Josh', phonebook)
        self.assertEqual(phonebook, {'Joshh':'956-333-2222'})
        self.assertEqual(len(phonebook), 1)
        delete_friend_phonebook('Joshhh', phonebook)
        self.assertEqual(len(phonebook), 1)

    def test_set_union(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])
        self.assertEqual(set1.union(set2), set([1,2,3,4,5,6]))

    def test_diff_union(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])
        self.assertEqual(set1.difference(set2), set([1,2]))

    def test_diff_union2(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])
        self.assertEqual(set2.difference(set1), set([5,6]))

    def test_set_symmetric_diff(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])
        self.assertEqual(set1.symmetric_difference(set2), set([1,2,5,6]))