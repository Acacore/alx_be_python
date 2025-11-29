import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(4, 3), 7)
    

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4, 3), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(12,3), 4)
        self.assertEqual(self.calc.divide(12,0), None)


        

    