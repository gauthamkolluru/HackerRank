import unittest
from factorial import facto

class test_facto(unittest.TestCase):
    def test_negative(self):
        self.assertEqual('Factorial cannot be computed for negative numbers', facto(-5))
    
    def test_zero(self):
        self.assertEqual(1, facto(0))
    
    def test_one(self):
        self.assertEqual(1, facto(1))
    
    def test_value(self):
        self.assertEqual(120, facto(5))
        self.assertEqual(2, facto(2))
        self.assertEqual(6, facto(3))

if __name__ == '__main__':
    unittest.main()