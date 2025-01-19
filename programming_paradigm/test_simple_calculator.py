import unittest
from simpleCalculator import SimpleCalculator




class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()

    def test_add(self):
        # result = SimpleCalculator.add(1, 2)
        self.assertEqual(self.calculator.add(2,1), 3)
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(2,1), 1)
    def multiplication(self):
        self.assertEqual(self.calculator.multiply(2,2), 4)
    def test_divide(self):
        self.assertEqual(self.calculator.divide(2,2), 1)



if __name__ == '__main__':
    unittest.main()