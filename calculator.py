"""
Calculator module.

This module provides basic arithmetic operations (addition, subtraction, multiplication, division)
and a utility to find the maximum of three numbers.
"""

def add(x, y):
    """
    Returns the sum of two numbers.
    :param x: First number
    :param y: Second number
    :return: Sum of x and y
    """
    return x + y


def subtract(x, y):
    """
    Returns the difference between two numbers.
    :param x: First number
    :param y: Second number
    :return: Difference (x - y)
    """
    return x - y


def multiply(x, y):
    """
    Returns the product of two numbers.
    :param x: First number
    :param y: Second number
    :return: Product of x and y
    """
    return x * y


def divide(x, y):
    """
    Returns the division of two numbers.
    Raises a ValueError if division by zero is attempted.
    :param x: Numerator
    :param y: Denominator
    :return: Quotient (x / y)
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def max_of_three(x, y, z):
    """
    Returns the maximum of three numbers.
    :param x: First number
    :param y: Second number
    :param z: Third number
    :return: Largest number among x, y, and z
    """
    return max(x, y, z)
