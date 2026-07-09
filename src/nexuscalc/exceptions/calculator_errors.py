"""Custom exceptions for the calculator."""

class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass

class DivisionByZeroError(CalculatorError):
    """Exception raised when attempting to divide by zero."""
    def __init__(self, message="Cannot divide by zero!"):
        self.message = message
        super().__init__(self.message)

class ParserError(CalculatorError):
    """Exception raised for parsing errors."""
    pass

class EvaluationError(CalculatorError):
    """Exception raised for evaluation errors."""
    pass

class InvalidInputError(CalculatorError):
    """Exception raised for invalid input."""
    pass

class OverflowError(CalculatorError):
    """Exception raised for numeric overflow."""
    pass
