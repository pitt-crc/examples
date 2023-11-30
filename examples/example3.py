"""Example 3: Reversing a string."""


def reverse_string(input_string):
    """Reverse the given string

    Args:
        input_string: The input string to be reversed

    Returns:
        The reversed string
    """

    reversed_str = ""

    for char in input_string.lower():
        reversed_str = char + reversed_str

    return reversed_str
