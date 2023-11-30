"""Answers for example 3."""

from unittest import TestCase

from examples.example3 import reverse_string


class TestReverseString(TestCase):

    def test_reverse_string(self):
        """Test basic reversal of a string"""

        result = reverse_string("hello")
        self.assertEqual(result, "olleh")

    def test_reverse_string_empty(self):
        """Test reversal of an empty string"""

        result = reverse_string("")
        self.assertEqual(result, "")

    def test_reverse_string_single_char(self):
        """Test reversal of a string with a single character"""

        result = reverse_string("a")
        self.assertEqual(result, "a")

    def test_reverse_string_whitespace(self):
        """Test reversal of a string with whitespace"""

        result = reverse_string("   spaces ")
        self.assertEqual(result, " secaps   ")

    def test_reverse_string_unicode(self):
        """Test reversal of a string with unicode characters"""

        result = reverse_string("héllo")
        self.assertEqual(result, "olléh")

    def test_reverse_string_mixed_case(self):
        """Test basic reversal of a string with mixed case"""

        result = reverse_string("AbCd")
        self.assertEqual(result, "dCbA")
