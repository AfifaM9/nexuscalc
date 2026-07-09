"""Tokenizer for mathematical expressions."""

import re
from .ast_nodes import Token

class Tokenizer:
    """Convert expression string into tokens."""
    
    def __init__(self):
        self.token_patterns = [
            ('NUMBER', r'\d+\.?\d*'),
            ('FUNCTION', r'(?:sqrt|sin|cos|tan|log|abs|ceil|floor|round)\b'),
            ('PLUS', r'\+'),
            ('MINUS', r'-'),
            ('MULTIPLY', r'\*'),
            ('DIVIDE', r'/'),
            ('FLOOR_DIVIDE', r'//'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('COMMA', r','),
            ('WHITESPACE', r'\s+'),
        ]
        self.token_regex = re.compile(
            '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_patterns)
        )
    
    def tokenize(self, expression):
        """Tokenize an expression string."""
        tokens = []
        position = 0
        line = 1
        col = 1
        
        for match in self.token_regex.finditer(expression):
            token_type = match.lastgroup
            value = match.group()
            
            if token_type == 'WHITESPACE':
                # Count newlines for position tracking
                lines = value.count('\n')
                if lines > 0:
                    line += lines
                    col = len(value) - value.rfind('\n') - 1
                else:
                    col += len(value)
                continue
            
            tokens.append(Token(token_type, value, position, line, col))
            position += len(value)
            col += len(value)
        
        return tokens
