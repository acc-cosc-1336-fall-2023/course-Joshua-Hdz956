import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
from tests.examples.j_classes import tests_classes
#from tests.homework.j_classes import tests_classes
#from tests.homework.d_repetition import tests_repetition

suite = unittest.TestLoader().loadTestsFromModule(tests_classes)
unittest.TextTestRunner(verbosity=2).run(suite)
