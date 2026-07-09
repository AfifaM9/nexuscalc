"""Expression parser for advanced calculations."""

import re
from ..exceptions.calculator_errors import ParserError
from .tokenizer import Tokenizer
from .ast_nodes import *

class ExpressionParser:
    """Parse mathematical expressions."""
    
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.current_token = None
        self.tokens = []
        self.position = 0
    
    def parse(self, expression):
        """Parse an expression string into an AST."""
        if not expression or expression.strip() == '':
            raise ParserError("Expression cannot be empty")
        
        self.tokens = self.tokenizer.tokenize(expression)
        self.position = 0
        
        if not self.tokens:
            raise ParserError("No valid tokens found in expression")
        
        self.current_token = self.tokens[0]
        return self.parse_expression()
    
    def parse_expression(self):
        """Parse an expression (addition/subtraction)."""
        node = self.parse_term()
        
        while self.current_token and self.current_token.type in ('PLUS', 'MINUS'):
            if self.current_token.type == 'PLUS':
                self.advance()
                right = self.parse_term()
                node = BinOpNode('+', node, right)
            elif self.current_token.type == 'MINUS':
                self.advance()
                right = self.parse_term()
                node = BinOpNode('-', node, right)
        
        return node
    
    def parse_term(self):
        """Parse a term (multiplication/division/floor)."""
        node = self.parse_factor()
        
        while self.current_token and self.current_token.type in ('MULTIPLY', 'DIVIDE', 'FLOOR_DIVIDE'):
            if self.current_token.type == 'MULTIPLY':
                self.advance()
                right = self.parse_factor()
                node = BinOpNode('*', node, right)
            elif self.current_token.type == 'DIVIDE':
                self.advance()
                right = self.parse_factor()
                node = BinOpNode('/', node, right)
            elif self.current_token.type == 'FLOOR_DIVIDE':
                self.advance()
                right = self.parse_factor()
                node = BinOpNode('//', node, right)
        
        return node
    
    def parse_factor(self):
        """Parse a factor (number, parenthesized expression, function call)."""
        if not self.current_token:
            raise ParserError("Unexpected end of expression")
        
        if self.current_token.type == 'NUMBER':
            value = self.current_token.value
            self.advance()
            return NumberNode(value)
        
        elif self.current_token.type == 'LPAREN':
            self.advance()
            node = self.parse_expression()
            if not self.current_token or self.current_token.type != 'RPAREN':
                raise ParserError("Missing closing parenthesis")
            self.advance()
            return node
        
        elif self.current_token.type == 'FUNCTION':
            func_name = self.current_token.value
            self.advance()
            if not self.current_token or self.current_token.type != 'LPAREN':
                raise ParserError(f"Missing parenthesis after function '{func_name}'")
            self.advance()
            args = []
            if self.current_token and self.current_token.type != 'RPAREN':
                args.append(self.parse_expression())
                while self.current_token and self.current_token.type == 'COMMA':
                    self.advance()
                    args.append(self.parse_expression())
            if not self.current_token or self.current_token.type != 'RPAREN':
                raise ParserError(f"Missing closing parenthesis for function '{func_name}'")
            self.advance()
            return FunctionNode(func_name, args)
        
        else:
            raise ParserError(f"Unexpected token: {self.current_token.type}")
    
    def advance(self):
        """Advance to the next token."""
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None
