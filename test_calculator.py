import unittest
from calculator import Calculator


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)

    def test_error_if_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
