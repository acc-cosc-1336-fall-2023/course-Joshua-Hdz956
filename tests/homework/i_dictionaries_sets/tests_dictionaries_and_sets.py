import unittest
from src.homework.i_dictionaries_sets.dictionary import get_p_distance, get_p_distance_matrix_for, get_p_distance_matrix_while
baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
class Test_Config(unittest.TestCase):
    """
    def test_p_distance(self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']
        self.assertEqual(get_p_distance(list1, list2),.4)
    
    def test_p_matrix_for(self):
        nested_list = [
        ['T','T','T','C','C','A','T','T','T','A'],
        ['G','A','T','T','C','A','T','T','T','C'],
        ['T','T','T','C','C','A','T','T','T','T'],
        ['G','T','T','C','C','A','T','T','T','A']
        ]
        values = [
        [0.0, 0.4, 0.1, 0.1],
        [0.4, 0.0, 0.4, 0.3],
        [0.1, 0.4, 0.0, 0.2],
        [0.1, 0.3, 0.2, 0.0]
        ]
        self.assertEqual(get_p_distance_matrix_for(nested_list), values)

    def test_p_matrix_while(self):
        nested_list = [
        ['T','T','T','C','C','A','T','T','T','A'],
        ['G','A','T','T','C','A','T','T','T','C'],
        ['T','T','T','C','C','A','T','T','T','T'],
        ['G','T','T','C','C','A','T','T','T','A']
        ]
        values = [
        [0.0, 0.4, 0.1, 0.1],
        [0.4, 0.0, 0.4, 0.3],
        [0.1, 0.4, 0.0, 0.2],
        [0.1, 0.3, 0.2, 0.0]
        ]
        self.assertEqual(get_p_distance_matrix_while(nested_list), values)
"""
    def test_play_both_sports(self):
        self.assertEqual(baseball.intersection(basketball), set(['Carmen','Alicia']))
        print("Play both sports: ", baseball.intersection(basketball))

    def test_play_either_sport(self):
        self.assertEqual(baseball.union(basketball),set(['Jodi','Carmen','Aida','Alicia','Eva','Sarah']))
        print("Play any sports: ", baseball.union(basketball))

    def test_play_baseball_not_basketball(self):
        self.assertEqual(baseball.difference(basketball),set(['Jodi','Aida']))
        print("Play Baseball but not Basketball: ", baseball.difference(basketball))


    def test_play_basket_not_base_also_play_base_not_basket(self):
        self.assertEqual(basketball.difference(baseball), set(['Eva','Sarah']))
        print("Play Basketball but not Baseball: ", basketball.difference(baseball))
        self.assertEqual(baseball.difference(basketball),set(['Jodi','Aida']))
        print("Play Baseball but not Basketball: ", baseball.difference(basketball))

    def test_play_one_sport_but_not_both(self):
        self.assertEqual(basketball.symmetric_difference(baseball), set(['Jodi','Aida','Eva','Sarah']))
        print("Play only one sport: ", basketball.symmetric_difference(baseball))
