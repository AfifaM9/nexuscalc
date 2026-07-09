"""Output formatting utilities."""

import math

def format_result(result):
    """Format the result for display."""
    if isinstance(result, float):
        # Handle special values
        if math.isnan(result):
            return "NaN (Not a Number)"
        if math.isinf(result):
            return "Infinity" if result > 0 else "-Infinity"
        
        # Remove trailing zeros for cleaner display
        if result.is_integer():
            return str(int(result))
        # Limit decimal places to 10
        return f"{result:.10f}".rstrip('0').rstrip('.')
    return str(result)

def format_expression(operation, num1, num2, result):
    """Format a complete mathematical expression."""
    symbols = {
        'add': '+',
        'subtract': '-',
        'multiply': '×',
        'divide': '÷',
        'floor': '//'
    }
    symbol = symbols.get(operation, '?')
    return f"{format_result(num1)} {symbol} {format_result(num2)} = {format_result(result)}"

def format_table(data, headers=None):
    """Format data as a table."""
    if not data:
        return ""
    
    if headers:
        rows = [headers] + data
    else:
        rows = data
    
    # Calculate column widths
    col_widths = []
    for col in range(len(rows[0])):
        max_width = max(len(str(row[col])) for row in rows)
        col_widths.append(max_width + 2)
    
    # Build table
    result = []
    for i, row in enumerate(rows):
        line = "|"
        for j, cell in enumerate(row):
            line += f" {str(cell).ljust(col_widths[j] - 1)}|"
        result.append(line)
        
        # Add header separator
        if i == 0 and headers:
            separator = "+"
            for width in col_widths:
                separator += "-" * width + "+"
            result.insert(1, separator)
    
    return "\n".join(result)
