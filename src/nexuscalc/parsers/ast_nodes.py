"""AST nodes for parsed expressions."""

from dataclasses import dataclass
from typing import List, Any, Optional

@dataclass
class Token:
    """Token representation."""
    type: str
    value: Any
    position: int = 0
    line: int = 1
    col: int = 1

class ASTNode:
    """Base class for AST nodes."""
    pass

@dataclass
class NumberNode(ASTNode):
    """Node for numeric values."""
    value: float
    
    def __str__(self):
        return str(self.value)

@dataclass
class BinOpNode(ASTNode):
    """Node for binary operations."""
    operator: str
    left: ASTNode
    right: ASTNode
    
    def __str__(self):
        return f"({self.left} {self.operator} {self.right})"

@dataclass
class UnaryOpNode(ASTNode):
    """Node for unary operations."""
    operator: str
    operand: ASTNode
    
    def __str__(self):
        return f"({self.operator}{self.operand})"

@dataclass
class FunctionNode(ASTNode):
    """Node for function calls."""
    name: str
    args: List[ASTNode]
    
    def __str__(self):
        args_str = ', '.join(str(arg) for arg in self.args)
        return f"{self.name}({args_str})"

@dataclass
class ConstantNode(ASTNode):
    """Node for constants like pi, e."""
    name: str
    value: float
    
    def __str__(self):
        return self.name
