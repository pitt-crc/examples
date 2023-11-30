"""Answers for example 2."""

import unittest

from examples.example2 import find_max


class TestFindMaxFunction(unittest.TestCase):
    """Test the `find_max` function."""

    def test_find_max_positive_numbers(self):
        """Test finding the maximum value in a list of positive numbers."""

        numbers = [10, 3, 2, 7, 5]
        result = find_max(numbers)
        self.assertEqual(result, 10)

    def test_find_max_negative_numbers(self):
        """Test finding the maximum value in a list of negative numbers."""

        numbers = [-3, -7, -2, -10, -5]
        result = find_max(numbers)
        self.assertEqual(result, -2)

    def test_find_max_mixed_numbers(self):
        """Test finding the maximum value in a list of mixed numbers."""

        numbers = [3, -7, 0, 10, -5]
        result = find_max(numbers)
        self.assertEqual(result, 10)

    def test_find_max_infinity(self):
        """Test finding the maximum value in a list that includes infinity."""

        numbers_with_infinity = [2, 5, float('inf'), 8, 1]
        result = find_max(numbers_with_infinity)
        self.assertEqual(result, float('inf'))

    def test_error_on_empty_list(self):
        """Test an IndexError is raised when finding max in an empty list."""

        with self.assertRaises(IndexError):
            find_max([])

    def test_find_max_imaginary_numbers(self):
        """Test a TypeError is raised for a list of imaginary numbers."""

        with self.assertRaises(TypeError):
            find_max([1j, 2j, 3j, 4j])
