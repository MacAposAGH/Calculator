"""Tests for calculator.py"""
import pytest
from  calculator import Calculator

class TestCalculator:
    """Tests for calculator.py"""

    calculator = Calculator(10, 5)

    def test_multiply(self):
        """Test multiplication"""
        assert self.calculator.multiply() == 50

    @pytest.mark.parametrize(
        "opt1, opt2, expected",
        [
            (2, 3, 6),
            (-2, 3, -6),
            (0, 5, 0),
            (2.5, 2, 5.0),
        ],
    )
    def test_multiply_parametrized(self, opt1, opt2, expected:int):
        """Test multiplication with different operands."""
        calculator = Calculator(opt1, opt2)
        assert calculator.multiply() == expected

    def test_divide(self):
        """Test division."""
        assert self.calculator.divide() == 2

    def test_divide_by_zero(self):
        """Test division by zero"""
        calculator = Calculator(3.0, 0)
        assert calculator.divide() is None

    def test_sum(self):
        """Test summation"""
        assert  self.calculator.sum() == 15

    def test_subtract(self):
        """Test subtraction"""
        assert self.calculator.subtract() == 5
