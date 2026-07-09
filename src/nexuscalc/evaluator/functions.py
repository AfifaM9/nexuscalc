"""Custom mathematical functions."""

import math
from functools import wraps
from nexuscalc.exceptions.calculator_errors import CalculatorError

class MathFunctions:
    """Collection of mathematical functions."""
    
    @staticmethod
    def sqrt(x):
        """Square root."""
        if x < 0:
            raise CalculatorError("Cannot take square root of negative number")
        return math.sqrt(x)
    
    @staticmethod
    def sin(x):
        """Sine in radians."""
        return math.sin(x)
    
    @staticmethod
    def cos(x):
        """Cosine in radians."""
        return math.cos(x)
    
    @staticmethod
    def tan(x):
        """Tangent in radians."""
        return math.tan(x)
    
    @staticmethod
    def log(x, base=math.e):
        """Logarithm with specified base."""
        if x <= 0:
            raise CalculatorError("Logarithm only defined for positive numbers")
        if base <= 0 or base == 1:
            raise CalculatorError("Logarithm base must be positive and not equal to 1")
        return math.log(x, base)
    
    @staticmethod
    def log10(x):
        """Base-10 logarithm."""
        return MathFunctions.log(x, 10)
    
    @staticmethod
    def log2(x):
        """Base-2 logarithm."""
        return MathFunctions.log(x, 2)
    
    @staticmethod
    def exp(x):
        """Exponential function e^x."""
        return math.exp(x)
    
    @staticmethod
    def pow(x, y):
        """Power function x^y."""
        return x ** y
    
    @staticmethod
    def factorial(x):
        """Factorial function."""
        if x < 0:
            raise CalculatorError("Factorial not defined for negative numbers")
        if not isinstance(x, int) and x.is_integer():
            x = int(x)
        if not isinstance(x, int):
            raise CalculatorError("Factorial only defined for integers")
        return math.factorial(x)
    
    @staticmethod
    def gcd(a, b):
        """Greatest common divisor."""
        return math.gcd(int(a), int(b))
    
    @staticmethod
    def lcm(a, b):
        """Least common multiple."""
        return abs(a * b) // math.gcd(int(a), int(b))
    
    @staticmethod
    def max(*args):
        """Maximum value."""
        return max(args)
    
    @staticmethod
    def min(*args):
        """Minimum value."""
        return min(args)
    
    @staticmethod
    def average(*args):
        """Average value."""
        if not args:
            raise CalculatorError("At least one number required for average")
        return sum(args) / len(args)
    
    @staticmethod
    def sum(*args):
        """Sum of numbers."""
        return sum(args)
    
    @staticmethod
    def product(*args):
        """Product of numbers."""
        result = 1
        for arg in args:
            result *= arg
        return result
    
    @staticmethod
    def is_prime(n):
        """Check if number is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
