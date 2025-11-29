import unittest
from simple_calculator import SimpleCalculator

class SimpleCalculator():
    ...

class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(SimpleCalculator.add(self, 4,3),7)

    def test_subtract(self):
        self.assertEqual(SimpleCalculator.subtract(self, 4,3),1)

    def test_multiply(self):
        self.assertEqual(SimpleCalculator.multiply(self, 4,3),12)
    
    def test_divide(self):
        self.assertEqual(SimpleCalculator.divide(self, 12,3), 4)
        self.assertEqual(SimpleCalculator.divide(self, 12,0), None)

    # def test_divide(self):
    #     with self.assertRaises(ZeroDivisionError):
    #         SimpleCalculator.divide(self, 12, 0)


        

    