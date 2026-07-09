"""Mathematical operations with proper error handling."""

from ..exceptions.calculator_errors import DivisionByZeroError, CalculatorError

class Operations:
    """Collection of mathematical operations."""
    
    @staticmethod
    def add(a, b):
        """Add two numbers."""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Subtract b from a."""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Divide a by b with zero division handling."""
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero!")
        if a == 0:
            return 0.0
        return a / b
    
    @staticmethod
    def floor_divide(a, b):
        """Floor divide a by b with zero division handling."""
        if b == 0:
            raise DivisionByZeroError("Cannot floor divide by zero!")
        if a == 0:
            return 0
        return a // b
    
    @staticmethod
    def safe_divide(a, b):
        """Safe division that returns None on error instead of raising."""
        try:
            return a / b
        except ZeroDivisionError:
            return None
    
    @staticmethod
    def safe_floor_divide(a, b):
        """Safe floor division that returns None on error instead of raising."""
        try:
            return a // b
        except ZeroDivisionError:
            return None
