"""Tests for expression parser."""

import pytest
from nexuscalc.parsers.expression_parser import ExpressionParser
from nexuscalc.parsers.tokenizer import Tokenizer
from nexuscalc.parsers.ast_nodes import Token, NumberNode, BinOpNode, FunctionNode
from nexuscalc.exceptions.calculator_errors import ParserError

def test_parser_initialization():
    parser = ExpressionParser()
    assert parser is not None
    assert parser.tokens == []
    assert parser.position == 0

def test_tokenizer_initialization():
    tokenizer = Tokenizer()
    assert tokenizer is not None
    assert tokenizer.token_regex is not None

def test_tokenizer_simple():
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize("2 + 3")
    assert len(tokens) >= 3
    assert tokens[0].type == 'NUMBER'
    assert tokens[0].value == '2'
    assert tokens[1].type == 'PLUS'
    assert tokens[2].type == 'NUMBER'
    assert tokens[2].value == '3'

def test_tokenizer_complex():
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize("2 + 3 * 4 / 5")
    assert len(tokens) >= 7
    assert tokens[0].type == 'NUMBER'
    assert tokens[1].type == 'PLUS'
    assert tokens[2].type == 'NUMBER'
    assert tokens[3].type == 'MULTIPLY'
    assert tokens[4].type == 'NUMBER'
    assert tokens[5].type == 'DIVIDE'
    assert tokens[6].type == 'NUMBER'

def test_tokenizer_with_parens():
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize("(2 + 3)")
    assert len(tokens) >= 5
    assert tokens[0].type == 'LPAREN'
    assert tokens[-1].type == 'RPAREN'

def test_tokenizer_with_function():
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize("sqrt(16)")
    assert len(tokens) >= 4
    assert tokens[0].type == 'FUNCTION'
    assert tokens[0].value == 'sqrt'
    assert tokens[1].type == 'LPAREN'
    assert tokens[2].type == 'NUMBER'
    assert tokens[2].value == '16'
    assert tokens[3].type == 'RPAREN'

def test_tokenizer_with_multiple_functions():
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize("sin(45) + cos(45)")
    function_count = sum(1 for t in tokens if t.type == 'FUNCTION')
    assert function_count == 2

def test_parser_simple_expression():
    parser = ExpressionParser()
    ast = parser.parse("2 + 3")
    assert isinstance(ast, BinOpNode)
    assert ast.operator == '+'
    assert isinstance(ast.left, NumberNode)
    assert ast.left.value == 2
    assert isinstance(ast.right, NumberNode)
    assert ast.right.value == 3

def test_parser_complex_expression():
    parser = ExpressionParser()
    ast = parser.parse("2 + 3 * 4")
    assert isinstance(ast, BinOpNode)
    assert ast.operator == '+'
    assert isinstance(ast.left, NumberNode)
    assert ast.left.value == 2
    assert isinstance(ast.right, BinOpNode)
    assert ast.right.operator == '*'
    assert ast.right.left.value == 3
    assert ast.right.right.value == 4

def test_parser_with_parentheses():
    parser = ExpressionParser()
    ast = parser.parse("(2 + 3) * 4")
    assert isinstance(ast, BinOpNode)
    assert ast.operator == '*'
    assert isinstance(ast.left, BinOpNode)
    assert ast.left.operator == '+'
    assert ast.left.left.value == 2
    assert ast.left.right.value == 3
    assert ast.right.value == 4

def test_parser_with_function():
    parser = ExpressionParser()
    ast = parser.parse("sqrt(16)")
    assert isinstance(ast, FunctionNode)
    assert ast.name == 'sqrt'
    assert len(ast.args) == 1
    assert isinstance(ast.args[0], NumberNode)
    assert ast.args[0].value == 16

def test_parser_empty_expression():
    parser = ExpressionParser()
    with pytest.raises(ParserError, match="Expression cannot be empty"):
        parser.parse("")
    with pytest.raises(ParserError, match="Expression cannot be empty"):
        parser.parse("   ")

def test_parser_invalid_expression():
    parser = ExpressionParser()
    with pytest.raises(ParserError):
        parser.parse("2 +")
    with pytest.raises(ParserError):
        parser.parse("+ 3")
    with pytest.raises(ParserError):
        parser.parse("2 + * 3")
