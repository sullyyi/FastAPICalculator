"""
Unit Tests for operations.py
Tests all arithmetic operations for correctness and error handling.
"""

import pytest
from operations import add, subtract, multiply, divide, power, logarithm, gcd, lcm


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


class TestLogarithm:
    """Test suite for logarithm operation"""
    
    def test_logarithm_base_10(self):
        """Test logarithm with base 10"""
        assert logarithm(100, 10) == 2
        assert logarithm(1000, 10) == 3
    
    def test_logarithm_base_2(self):
        """Test logarithm with base 2"""
        assert logarithm(8, 2) == 3
        assert logarithm(16, 2) == 4
    
    def test_logarithm_natural(self):
        """Test natural logarithm (base e)"""
        import math
        assert logarithm(math.e, math.e) == pytest.approx(1)
    
    def test_logarithm_fractional_argument(self):
        """Test logarithm with fractional argument"""
        assert logarithm(0.5, 2) == pytest.approx(-1)
        assert logarithm(0.1, 10) == pytest.approx(-1)
    
    def test_logarithm_one_returns_zero(self):
        """Test that log of 1 is always 0"""
        assert logarithm(1, 10) == 0
        assert logarithm(1, 2) == 0
        assert logarithm(1, 100) == 0
    
    def test_logarithm_invalid_argument_zero(self):
        """Test logarithm with argument of 0 raises ValueError"""
        with pytest.raises(ValueError, match="Logarithm argument must be greater than 0"):
            logarithm(0, 10)
    
    def test_logarithm_invalid_argument_negative(self):
        """Test logarithm with negative argument raises ValueError"""
        with pytest.raises(ValueError, match="Logarithm argument must be greater than 0"):
            logarithm(-5, 10)
    
    def test_logarithm_invalid_base_zero(self):
        """Test logarithm with base of 0 raises ValueError"""
        with pytest.raises(ValueError, match="Logarithm base must be greater than 0"):
            logarithm(100, 0)
    
    def test_logarithm_invalid_base_negative(self):
        """Test logarithm with negative base raises ValueError"""
        with pytest.raises(ValueError, match="Logarithm base must be greater than 0"):
            logarithm(100, -2)
    
    def test_logarithm_invalid_base_one(self):
        """Test logarithm with base of 1 raises ValueError"""
        with pytest.raises(ValueError, match="Logarithm base cannot be 1"):
            logarithm(100, 1)


class TestGCD:
    """Test suite for GCD operation"""
    
    def test_gcd_basic(self):
        """Test basic GCD calculations"""
        assert gcd(12, 8) == 4
        assert gcd(21, 14) == 7
    
    def test_gcd_coprime(self):
        """Test GCD of coprime numbers (GCD = 1)"""
        assert gcd(7, 11) == 1
        assert gcd(13, 17) == 1
    
    def test_gcd_one_number_zero_times_another(self):
        """Test GCD where one number is multiple of another"""
        assert gcd(10, 5) == 5
        assert gcd(20, 5) == 5
    
    def test_gcd_same_numbers(self):
        """Test GCD of identical numbers"""
        assert gcd(5, 5) == 5
        assert gcd(100, 100) == 100
    
    def test_gcd_with_float_integers(self):
        """Test GCD with float values that are integers"""
        assert gcd(12.0, 8.0) == 4
        assert gcd(20.0, 15.0) == 5
    
    def test_gcd_invalid_float(self):
        """Test GCD with non-integer float raises ValueError"""
        with pytest.raises(ValueError, match="GCD requires integer arguments"):
            gcd(12.5, 8)
    
    def test_gcd_invalid_negative(self):
        """Test GCD with negative numbers raises ValueError"""
        with pytest.raises(ValueError, match="GCD requires positive integers"):
            gcd(-12, 8)
    
    def test_gcd_invalid_zero(self):
        """Test GCD with zero raises ValueError"""
        with pytest.raises(ValueError, match="GCD requires positive integers"):
            gcd(0, 8)


class TestLCM:
    """Test suite for LCM operation"""
    
    def test_lcm_basic(self):
        """Test basic LCM calculations"""
        assert lcm(12, 8) == 24
        assert lcm(4, 6) == 12
    
    def test_lcm_coprime(self):
        """Test LCM of coprime numbers"""
        assert lcm(7, 11) == 77
        assert lcm(3, 5) == 15
    
    def test_lcm_one_divides_other(self):
        """Test LCM where one number divides the other"""
        assert lcm(10, 5) == 10
        assert lcm(20, 5) == 20
    
    def test_lcm_same_numbers(self):
        """Test LCM of identical numbers"""
        assert lcm(5, 5) == 5
        assert lcm(100, 100) == 100
    
    def test_lcm_with_float_integers(self):
        """Test LCM with float values that are integers"""
        assert lcm(12.0, 8.0) == 24
        assert lcm(4.0, 6.0) == 12
    
    def test_lcm_invalid_float(self):
        """Test LCM with non-integer float raises ValueError"""
        with pytest.raises(ValueError, match="LCM requires integer arguments"):
            lcm(12.5, 8)
    
    def test_lcm_invalid_negative(self):
        """Test LCM with negative numbers raises ValueError"""
        with pytest.raises(ValueError, match="LCM requires positive integers"):
            lcm(-12, 8)
    
    def test_lcm_invalid_zero(self):
        """Test LCM with zero raises ValueError"""
        with pytest.raises(ValueError, match="LCM requires positive integers"):
            lcm(0, 8)
