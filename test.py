import unittest
import unit_testing 


class test_unit(unittest.TestCase):
    def test_add(self):
        result = unit_testing.add(25,10)
        self.assertEqual(result, 15)