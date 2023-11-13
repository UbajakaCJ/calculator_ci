"""
Unit tests for the calculator library
"""

import calculator

# class TestCalculator:

#     def test_addition(self):
#         assert 4 == calculator.add(2, 2)

#     def test_subtraction(self):
#         assert 2 == calculator.subtract(4, 2)


import unittest

class MyTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.add(2, 2), 4)
    
    def test_subtraction(self):
        self.assertEqual(calculator.subtract(5, 3), 2)

if __name__ == '__main__':
    unittest.main()