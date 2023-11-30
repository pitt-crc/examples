"""Tests for the `calculator.add` method."""

from unittest import TestCase

from examples.calculator.math import add


class TestAdd(TestCase):
    """Test case for the add function in the calculator module."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""

        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""

        result = add(-2, -4)
        self.assertEqual(result, -6)

    def test_add_mixed_numbers(self):
        """Test adding a positive and a negative number."""

        result = add(10, -7)
        self.assertEqual(result, 3)
