import pytest

from  calculator import Calculator
class TestCalculator:


    # @pytest.mark.parametrize(
    #     "opt1, opt2, expected",
    #     [
    #         (10, 5, 5),
    #     ]
    # )
    # def test_subtract(opt1, opt2, expected):
    #     calc = Calculator(opt1, opt2)
    #
    #     assert calc.subtract() == expected

    def test_sum(self):
        assert self.calc.sum() == 5.0

    def test_multiply(self):
        assert self.calc.multiply() == 6.0

    def test_divide(self):
        assert self.calc.divide() == 1.5

    def test_divide_by_zero(self):
        calc = Calculator(3.0, 0)
        assert calc.divide() is None
