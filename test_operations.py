"""
Unit Tests for operations.py
Tests all arithmetic operations for correctness and error handling.
"""

import pytest
from operations import add, subtract, multiply, divide, power


class TestAddition:
    """Test suite for addition operation"""
    
    def test_add_positive_integers(self):
        """Test adding two positive integers"""
        assert add(2, 3) == 5
    
    def test_add_negative_integers(self):
        """Test adding two negative integers"""
        assert add(-2, -3) == -5
    
    def test_add_mixed_integers(self):
        """Test adding positive and negative integers"""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
    
    def test_add_floats(self):
        """Test adding floating point numbers"""
        assert add(2.5, 3.5) == 6.0
        assert add(0.1, 0.2) == pytest.approx(0.3)
    
    def test_add_zero(self):
        """Test adding zero"""
        assert add(5, 0) == 5
        assert add(0, 0) == 0


class TestSubtraction:
    """Test suite for subtraction operation"""
    
    def test_subtract_positive_integers(self):
        """Test subtracting two positive integers"""
        assert subtract(5, 3) == 2
    
    def test_subtract_negative_integers(self):
        """Test subtracting two negative integers"""
        assert subtract(-5, -3) == -2
    
    def test_subtract_mixed_integers(self):
        """Test subtracting positive and negative integers"""
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8
    
    def test_subtract_floats(self):
        """Test subtracting floating point numbers"""
        assert subtract(5.5, 2.5) == 3.0
    
    def test_subtract_zero(self):
        """Test subtracting zero"""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5


class TestMultiplication:
    """Test suite for multiplication operation"""
    
    def test_multiply_positive_integers(self):
        """Test multiplying two positive integers"""
        assert multiply(3, 4) == 12
    
    def test_multiply_negative_integers(self):
        """Test multiplying two negative integers"""
        assert multiply(-3, -4) == 12
    
    def test_multiply_mixed_integers(self):
        """Test multiplying positive and negative integers"""
        assert multiply(3, -4) == -12
        assert multiply(-3, 4) == -12
    
    def test_multiply_floats(self):
        """Test multiplying floating point numbers"""
        assert multiply(2.5, 4.0) == 10.0
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero"""
        assert multiply(5, 0) == 0
        assert multiply(0, 0) == 0
    
    def test_multiply_by_one(self):
        """Test multiplying by one"""
        assert multiply(5, 1) == 5


class TestDivision:
    """Test suite for division operation"""
    
    def test_divide_positive_integers(self):
        """Test dividing two positive integers"""
        assert divide(10, 2) == 5
    
    def test_divide_negative_integers(self):
        """Test dividing two negative integers"""
        assert divide(-10, -2) == 5
    
    def test_divide_mixed_integers(self):
        """Test dividing positive and negative integers"""
        assert divide(10, -2) == -5
        assert divide(-10, 2) == -5
    
    def test_divide_floats(self):
        """Test dividing floating point numbers"""
        assert divide(10.0, 2.5) == 4.0
    
    def test_divide_by_zero(self):
        """Test dividing by zero raises ValueError"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
    
    def test_divide_zero_by_number(self):
        """Test dividing zero by a number"""
        assert divide(0, 5) == 0
    
    def test_divide_result_float(self):
        """Test division always returns float result"""
        result = divide(5, 2)
        assert result == 2.5
        assert isinstance(result, float)


class TestPower:
    """Test suite for power operation"""
    
    def test_power_positive_integers(self):
        """Test raising positive integer to positive power"""
        assert power(2, 3) == 8
        assert power(5, 2) == 25
    
    def test_power_negative_base(self):
        """Test raising negative base to power"""
        assert power(-2, 3) == -8
        assert power(-2, 2) == 4
    
    def test_power_zero_exponent(self):
        """Test raising any number to power of zero"""
        assert power(5, 0) == 1
        assert power(-5, 0) == 1
    
    def test_power_zero_base(self):
        """Test raising zero to positive power"""
        assert power(0, 5) == 0
    
    def test_power_fractional_exponent(self):
        """Test raising number to fractional power"""
        assert power(4, 0.5) == 2.0  # Square root
        assert power(8, 1/3) == pytest.approx(2.0)  # Cube root
    
    def test_power_negative_exponent(self):
        """Test raising number to negative power"""
        assert power(2, -1) == 0.5
        assert power(10, -2) == 0.01
    
    def test_power_floats(self):
        """Test power operation with floats"""
        assert power(2.5, 2) == 6.25


class TestEdgeCases:
    """Test suite for edge cases"""
    
    def test_large_numbers(self):
        """Test operations with large numbers"""
        assert add(1e10, 1e10) == 2e10
        assert multiply(1e5, 1e5) == 1e10
    
    def test_very_small_numbers(self):
        """Test operations with very small numbers"""
        result = add(1e-10, 1e-10)
        assert result == pytest.approx(2e-10)
    
    def test_mixed_int_float(self):
        """Test operations mixing int and float"""
        assert add(5, 2.5) == 7.5
        assert subtract(5, 2.5) == 2.5
        assert multiply(4, 2.5) == 10.0
        assert divide(5, 2) == 2.5
