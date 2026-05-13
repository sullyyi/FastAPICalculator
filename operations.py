"""
Module for basic arithmetic operations.
Provides functions for fundamental mathematical calculations with logging support.
"""

import logging
import math
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


def logarithm(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Calculate the logarithm of a number with a given base.
    
    Args:
        a: The argument (must be > 0)
        b: The base (must be > 0 and not equal to 1)
    
    Returns:
        Logarithm of a with base b
    
    Raises:
        ValueError: If argument or base is invalid
    """
    if a <= 0:
        logger.error(f"Logarithm with invalid argument: log_{b}({a})")
        raise ValueError("Logarithm argument must be greater than 0")
    
    if b <= 0:
        logger.error(f"Logarithm with invalid base: log_{b}({a})")
        raise ValueError("Logarithm base must be greater than 0")
    
    if b == 1:
        logger.error(f"Logarithm with invalid base: log_{b}({a})")
        raise ValueError("Logarithm base cannot be 1")
    
    result = math.log(a, b)
    logger.info(f"Logarithm: log_{b}({a}) = {result}")
    return result


def gcd(a: Union[int, float], b: Union[int, float]) -> int:
    """
    Calculate the greatest common divisor of two integers.
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        Greatest common divisor of a and b
    
    Raises:
        ValueError: If arguments are not integers or are not positive
    """
    # Check if inputs are integers (or can be converted to integers)
    if not isinstance(a, int) or not isinstance(b, int):
        if isinstance(a, float) and a.is_integer():
            a = int(a)
        else:
            logger.error(f"GCD requires integers: gcd({a}, {b})")
            raise ValueError("GCD requires integer arguments")
        
        if isinstance(b, float) and b.is_integer():
            b = int(b)
        else:
            logger.error(f"GCD requires integers: gcd({a}, {b})")
            raise ValueError("GCD requires integer arguments")
    
    if a <= 0 or b <= 0:
        logger.error(f"GCD requires positive integers: gcd({a}, {b})")
        raise ValueError("GCD requires positive integers")
    
    result = math.gcd(a, b)
    logger.info(f"GCD: gcd({a}, {b}) = {result}")
    return result


def lcm(a: Union[int, float], b: Union[int, float]) -> int:
    """
    Calculate the least common multiple of two integers.
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        Least common multiple of a and b
    
    Raises:
        ValueError: If arguments are not integers or are not positive
    """
    # Check if inputs are integers (or can be converted to integers)
    if not isinstance(a, int) or not isinstance(b, int):
        if isinstance(a, float) and a.is_integer():
            a = int(a)
        else:
            logger.error(f"LCM requires integers: lcm({a}, {b})")
            raise ValueError("LCM requires integer arguments")
        
        if isinstance(b, float) and b.is_integer():
            b = int(b)
        else:
            logger.error(f"LCM requires integers: lcm({a}, {b})")
            raise ValueError("LCM requires integer arguments")
    
    if a <= 0 or b <= 0:
        logger.error(f"LCM requires positive integers: lcm({a}, {b})")
        raise ValueError("LCM requires positive integers")
    
    # LCM formula: lcm(a,b) = (a*b) / gcd(a,b)
    result = abs(a * b) // math.gcd(a, b)
    logger.info(f"LCM: lcm({a}, {b}) = {result}")
    return result
