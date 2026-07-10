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
        """Square root operation."""
        if a < 0:
            raise CalculatorError("Cannot take square root of a negative number!")
        return math.sqrt(a)
    
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
