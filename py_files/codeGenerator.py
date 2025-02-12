from llvmlite import ir
from AST import *

class LLVMCodeGen:
    def __init__(self):
        self.module = ir.Module(name="my_module")
        self.builder = None
        self.func = None
        self.symbol_table = {}

    def generate_code(self, node):
        """Recursively generates LLVM IR for an AST node."""
        if isinstance(node, ProgramNode):
            return self.generate_code(node.expr)

        elif isinstance(node, BinaryOpNode):
            left = self.generate_code(node.left)
            right = self.generate_code(node.right)

            if self.builder:
                if node.op == "+":
                    return self.builder.add(left, right, name="addtmp")
                elif node.op == "-":
                    return self.builder.sub(left, right, name="subtmp")
                elif node.op == "*":
                    return self.builder.mul(left, right, name="multmp")
                elif node.op == "/":
                    return self.builder.sdiv(left, right, name="divtmp")

        elif isinstance(node, IdentifierNode):
            if node.name.isdigit():
                return ir.Constant(ir.IntType(32), int(node.name))
            else:
                if node.name in self.symbol_table:
                    return self.builder.load(self.symbol_table[node.name], name="loadtmp")
                else:
                    raise ValueError(f"Undefined variable: {node.name}")

        elif isinstance(node, ParenExprNode):
            return self.generate_code(node.expr)

    def compile(self, ast):
        """Creates an LLVM function to compute the expression."""
        func_type = ir.FunctionType(ir.IntType(32), [])
        self.func = ir.Function(self.module, func_type, name="main")

        block = self.func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        result = self.generate_code(ast)
        self.builder.ret(result)

        return str(self.module)

    def save_ir_to_file(self, filename="generated_code.ll"):
        """Save the generated LLVM IR to a file."""
        with open(filename, "w") as f:
            f.write(str(self.module))
