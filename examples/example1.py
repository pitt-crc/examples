"""Example 1: Dividing two numbers."""


def divide(x: float, y: float) -> float:
    """Divide two numbers

    Return float('inf') when dividing by zero.

    Args:
        x: The numerator
        y: The denominator

    Returns:
        The quotient of x and y
    """

    if y == 0:
        return float('inf')

    return x // y
