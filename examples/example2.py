"""Example 1: Finding the maximum value."""


def find_max(input_list: list):
    """Find the maximum value in a list.

    Args:
        input_list: The input list of numbers.

    Returns:
        int or float: The maximum value in the list.

    Raises:
        IndexError: For an empty list
    """

    max_value = input_list[1]

    for num in input_list[1:]:
        if num > max_value:
            max_value = num

    return max_value
