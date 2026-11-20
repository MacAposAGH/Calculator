class Calculator:
    """A simple calculator supporting basic arithmetic operations."""
    def __init__(self, opt1, opt2):
        self._opt1 = opt1
        self._opt2 = opt2

    def multiply(self) -> float:
        """Multiply the first operand by the second."""
        return self._opt1 * self._opt2

    def divide(self) -> float | None:
        """Divide the first operand by the second."""
        try:
            return self._opt1 / self._opt2
        except ZeroDivisionError:
            return None

    def sum(self) -> float:
        """Sum the first operand by the second."""
        return self._opt1 + self._opt2

    def subtract(self) -> float:
        """Subtract the second operand from the first."""
        return self._opt1 - self._opt2
