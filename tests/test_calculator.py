"""Tests for calculator core functionality."""

import pytest
from nexuscalc.core.calculator import NexusCalc
from nexuscalc.core.operations import Operations
from nexuscalc.exceptions.calculator_errors import CalculatorError, DivisionByZeroError

def test_add():
    ops = Operations()
    assert ops.add(5, 3) == 8
    assert ops.add(-1, 1) == 0
    assert ops.add(2.5, 3.5) == 6.0
    assert ops.add(0, 0) == 0

def test_subtract():
    ops = Operations()
    assert ops.subtract(10, 4) == 6
    assert ops.subtract(0, 5) == -5
    assert ops.subtract(3.5, 1.5) == 2.0
    assert ops.subtract(-5, -3) == -2

def test_multiply():
    ops = Operations()
    assert ops.multiply(3, 4) == 12
    assert ops.multiply(-2, 3) == -6
    assert ops.multiply(2.5, 2) == 5.0
    assert ops.multiply(0, 5) == 0
    assert ops.multiply(-2, -3) == 6

def test_divide():
    ops = Operations()
    assert ops.divide(10, 2) == 5
    assert ops.divide(7, 2) == 3.5
    assert ops.divide(0, 5) == 0.0
    
    with pytest.raises(DivisionByZeroError, match="Cannot divide by zero!"):
        ops.divide(5, 0)
    
    with pytest.raises(DivisionByZeroError):
        ops.divide(5, 0)

def test_floor_divide():
    ops = Operations()
    assert ops.floor_divide(10, 3) == 3
    assert ops.floor_divide(-10, 3) == -4
    assert ops.floor_divide(0, 5) == 0
    
    with pytest.raises(DivisionByZeroError, match="Cannot floor divide by zero!"):
        ops.floor_divide(5, 0)

def test_safe_divide():
    ops = Operations()
    assert ops.safe_divide(10, 2) == 5
    assert ops.safe_divide(5, 0) is None
    assert ops.safe_divide(0, 5) == 0.0

def test_safe_floor_divide():
    ops = Operations()
    assert ops.safe_floor_divide(10, 3) == 3
    assert ops.safe_floor_divide(5, 0) is None

def test_calculator_init():
    calc = NexusCalc()
    assert calc.running == True
    assert len(calc.menu_options) == 5
    assert '1' in calc.menu_options
    assert '2' in calc.menu_options
    assert '3' in calc.menu_options
    assert '4' in calc.menu_options
    assert '5' in calc.menu_options

def test_calculator_menu_options():
    calc = NexusCalc()
    assert calc.menu_options['1'][0] == 'Add'
    assert calc.menu_options['2'][0] == 'Subtract'
    assert calc.menu_options['3'][0] == 'Multiply'
    assert calc.menu_options['4'][0] == 'Divide'
    assert calc.menu_options['5'][0] == 'Floor'

def test_division_by_zero_error_inheritance():
    """Test that DivisionByZeroError is properly inherited from CalculatorError."""
    assert issubclass(DivisionByZeroError, CalculatorError)
    
    try:
        raise DivisionByZeroError("Test error")
    except CalculatorError:
        pass
    except Exception:
        pytest.fail("DivisionByZeroError should be caught by CalculatorError")
