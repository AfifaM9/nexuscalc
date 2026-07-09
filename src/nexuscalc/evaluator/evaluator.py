"""Expression evaluator for advanced calculations."""

import math
from ..exceptions.calculator_errors import EvaluationError, DivisionByZeroError
from ..parsers.ast_nodes import NumberNode, BinOpNode, UnaryOpNode, FunctionNode, ConstantNode
from ..core.constants import Constants

class Evaluator:
    """Evaluate parsed expressions."""
    
    def __init__(self):
        self.constants = Constants()
        self.functions = {
            'sqrt': math.sqrt,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log,
            'abs': abs,
            'ceil': math.ceil,
            'floor': math.floor,
            'round': round,
        }
    
    def evaluate(self, ast):
        """Evaluate an AST and return the result."""
        if isinstance(ast, NumberNode):
            return ast.value
        
        elif isinstance(ast, BinOpNode):
            left_val = self.evaluate(ast.left)
            right_val = self.evaluate(ast.right)
            
            if ast.operator == '+':
                return left_val + right_val
            elif ast.operator == '-':
                return left_val - right_val
            elif ast.operator == '*':
                return left_val * right_val
            elif ast.operator == '/':
                if right_val == 0:
                    raise DivisionByZeroError("Division by zero in expression")
                return left_val / right_val
            elif ast.operator == '//':
                if right_val == 0:
                    raise DivisionByZeroError("Floor division by zero in expression")
                return left_val // right_val
            else:
                raise EvaluationError(f"Unknown binary operator: {ast.operator}")
        
        elif isinstance(ast, UnaryOpNode):
            operand_val = self.evaluate(ast.operand)
            if ast.operator == '-':
                return -operand_val
            elif ast.operator == '+':
                return +operand_val
            else:
                raise EvaluationError(f"Unknown unary operator: {ast.operator}")
        
        elif isinstance(ast, FunctionNode):
            args = [self.evaluate(arg) for arg in ast.args]
            if ast.name in self.functions:
                try:
                    return self.functions[ast.name](*args)
                except Exception as e:
                    raise EvaluationError(f"Error evaluating function {ast.name}: {e}")
            else:
                raise EvaluationError(f"Unknown function: {ast.name}")
        
        elif isinstance(ast, ConstantNode):
            return ast.value
        
        else:
            raise EvaluationError(f"Unknown AST node type: {type(ast)}")
    
    def evaluate_expression(self, expression):
        """Convenience method to parse and evaluate an expression."""
        from ..parsers.expression_parser import ExpressionParser
        parser = ExpressionParser()
        ast = parser.parse(expression)
        return self.evaluate(ast)
