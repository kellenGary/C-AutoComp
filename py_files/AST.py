class ASTNode:
    """Base class for all AST nodes."""
    pass

class ProgramNode(ASTNode):
    """Represents a program (expr SEMICOLON)."""
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"ProgramNode({self.expr})"

class BinaryOpNode(ASTNode):
    """Represents a binary operation (e.g., addition, subtraction)."""
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinaryOpNode({self.left}, {self.op}, {self.right})"

class IdentifierNode(ASTNode):
    """Represents an identifier (e.g., a variable name)."""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"IdentifierNode({self.name})"

class ParenExprNode(ASTNode):
    """Represents a parenthesized expression."""
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"ParenExprNode({self.expr})"
