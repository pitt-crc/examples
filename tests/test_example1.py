"""Answers for example 1."""

import unittest

from examples.example1 import divide


class TestDivideFunction(unittest.TestCase):
    """Test the `divide` function"""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""

        result = divide(8, 2)
        self.assertEqual(result, 4.0)

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""

        result = divide(-6, 3)
        self.assertEqual(result, -2.0)

    def test_divide_float_numbers(self):
        """Test dividing float numbers."""

        result = divide(5.5, 2.2)
        self.assertAlmostEqual(result, 2.5, delta=0.001)

    def test_divide_by_zero(self):
        """Test dividing by zero."""

        result = divide(10, 0)
        self.assertEqual(result, float('inf'))
