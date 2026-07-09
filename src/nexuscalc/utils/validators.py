"""Input validation utilities."""

import math
from ..exceptions.calculator_errors import CalculatorError

def validate_number(value):
    """Validate and convert a string to a number (int or float)."""
    if not value or value.strip() == '':
        raise CalculatorError("Input cannot be empty")
    
    value = value.strip().lower()
    
    # Check for special values
    if value in ['inf', 'infinity']:
        return float('inf')
    if value == '-inf':
        return float('-inf')
    if value in ['nan', 'not a number']:
        return float('nan')
    
    try:
        # Try int first
        return int(value)
    except ValueError:
        try:
            # Try float
            return float(value)
        except ValueError:
            raise CalculatorError(f"'{value}' is not a valid number")
    
def is_valid_number(value):
    """Check if a value is a valid number (not NaN or Infinity)."""
    if isinstance(value, (int, float)):
        return not (math.isnan(value) or math.isinf(value))
    return False

def is_integer(value):
    """Check if a value is an integer."""
    if isinstance(value, int):
        return True
    if isinstance(value, float):
        return value.is_integer()
    return False
