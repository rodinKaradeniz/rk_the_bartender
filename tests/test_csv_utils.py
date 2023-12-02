import unittest
from data_processing import csv_utils


class TestCsvUtils(unittest.TestCase):
    def test_refactor_ingredient_name(self):
        self.assertEqual(csv_utils.refactor_ingredient_name('VODKA'), 'vodka')
        self.assertEqual(csv_utils.refactor_ingredient_name('  w h i S k Ey   '), 'whiskey')

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()