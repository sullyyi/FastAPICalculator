"""
Module for basic arithmetic operations.
Provides functions for fundamental mathematical calculations with logging support.
"""

import logging
from typing import Union

# Configure logging
logger = logging.getLogger(__name__)


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        Sum of a and b
    """
    result = a + b
    logger.info(f"Addition: {a} + {b} = {result}")
    return result


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtract two numbers.
    
    Args:
        a: First number (int or float)
        b: Second number to subtract (int or float)
    
    Returns:
        Difference of a and b
    """
    result = a - b
    logger.info(f"Subtraction: {a} - {b} = {result}")
    return result


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiply two numbers.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        Product of a and b
    """
    result = a * b
    logger.info(f"Multiplication: {a} * {b} = {result}")
    return result


def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Divide two numbers.
    
    Args:
        a: Numerator (int or float)
        b: Denominator (int or float)
    
    Returns:
        Quotient of a and b
    
    Raises:
        ValueError: If attempting to divide by zero
    """
    if b == 0:
        logger.error(f"Division by zero attempted: {a} / {b}")
        raise ValueError("Cannot divide by zero")
    
    result = a / b
    logger.info(f"Division: {a} / {b} = {result}")
    return result


def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """
    Raise a number to a power.
    
    Args:
        base: Base number (int or float)
        exponent: Exponent (int or float)
    
    Returns:
        Base raised to the power of exponent
    """
    result = base ** exponent
    logger.info(f"Power: {base} ^ {exponent} = {result}")
    return result
