import unittest
import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        result = SimpleCalculator.add(1, 2)
        self.assertEqual(result, 3)
    def test_subtract(self):
        result = SimpleCalculator.subtract(5, 1)
        self.assertEqual(result, 4)



if __name__ == '__main__':
    unittest.main()