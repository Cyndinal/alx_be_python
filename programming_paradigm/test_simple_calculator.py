import unittest
from simple_calculator import SimpleCalculator




class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,1), 3)
"""
        ["test_addition", " self.assertEqual(self.calc.add", "test_addition(self)"]
"""
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2,1), 1)
    def multiplication(self):
        self.assertEqual(self.calc.multiply(2,2), 4)
    def test_divide(self):
        self.assertEqual(self.calc.divide(2,2), 1)



if __name__ == '__main__':
    unittest.main()