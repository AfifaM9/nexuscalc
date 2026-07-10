"""Mathematical operations with proper error handling."""

import math
from ..exceptions.calculator_errors import DivisionByZeroError, CalculatorError

class Operations:
    """Collection of mathematical operations."""
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero!")
        if a == 0:
            return 0.0
        return a / b
    
    @staticmethod
    def floor_divide(a, b):
        if b == 0:
            raise DivisionByZeroError("Cannot floor divide by zero!")
        if a == 0:
            return 0
        return a // b
    
    @staticmethod
    def modulo(a, b):
        if b == 0:
            raise DivisionByZeroError("Cannot perform modulo by zero!")
        return a % b
    
    @staticmethod
    def exponent(a, b):
        return a ** b
    
    @staticmethod
    def square_root(a):
        if a < 0:
            raise CalculatorError("Cannot take square root of a negative number!")
        return math.sqrt(a)
    
    @staticmethod
    def nth_root(a, n):
        """Nth root operation - returns the nth root of a."""
        if n == 0:
            raise CalculatorError("Root cannot be zero!")
        if a < 0 and n % 2 == 0:
            raise CalculatorError("Cannot take even root of a negative number!")
        if a < 0:
            return -abs(a) ** (1/n)
        return a ** (1/n)
    
    @staticmethod
    def percentage(a, b):
        """Percentage operation - returns a% of b."""
        return (a / 100) * b
    
    @staticmethod
    def factorial(n):
        """Factorial operation - returns n!."""
        if n < 0:
            raise CalculatorError("Factorial is not defined for negative numbers!")
        if n != int(n):
            raise CalculatorError("Factorial is only defined for integers!")
        n = int(n)
        if n > 100:
            raise CalculatorError("Factorial too large to compute!")
        return math.factorial(n)
    
    @staticmethod
    def safe_divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return None
    
    @staticmethod
    def safe_floor_divide(a, b):
        try:
            return a // b
        except ZeroDivisionError:
            return None
    
    @staticmethod
    def safe_modulo(a, b):
        try:
            return a % b
        except ZeroDivisionError:
            return None
    
    @staticmethod
    def safe_exponent(a, b):
        try:
            return a ** b
        except Exception:
            return None
    
    @staticmethod
    def safe_square_root(a):
        try:
            if a < 0:
                return None
            return math.sqrt(a)
        except Exception:
            return None
    
    @staticmethod
    def safe_nth_root(a, n):
        try:
            if n == 0:
                return None
            if a < 0 and n % 2 == 0:
                return None
            if a < 0:
                return -abs(a) ** (1/n)
            return a ** (1/n)
        except Exception:
            return None
    
    @staticmethod
    def safe_percentage(a, b):
        try:
            return (a / 100) * b
        except Exception:
            return None
    
    @staticmethod
    def safe_factorial(n):
        try:
            if n < 0 or n != int(n) or n > 100:
                return None
            return math.factorial(int(n))
        except Exception:
            return None
