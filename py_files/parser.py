from stack import Stack
from parsetab import _lr_action, _lr_goto, _lr_productions
from tokenizer import Token
from ErrorRecovery import fixTokens
from AST import *

class Parser:
    """LR(1) PARSER"""
    def __init__(self):
        self.stack = Stack()
        self.state_stack = [0]
        self.input_buffer = []

    def parse(self, tokens):
        self.input_buffer = tokens + [Token('$end', None)]
        copied_buffer = self.input_buffer
        while True:
            current_state = self.state_stack[-1]
            next_token = self.input_buffer[0]
            next_type = next_token.type

            # Error Recovery Step
            if next_type not in _lr_action[current_state]:
                print(f"Syntax error: Unexpected token {next_type}")
                # Attempt error recovery
                tokens_left = len(self.input_buffer)
                new_tokens = fixTokens(self.stack, next_token, copied_buffer, tokens_left)
                self.input_buffer.insert(0, new_tokens)
                continue

            action = _lr_action[current_state][next_type]

            if action > 0:
                # Shift operation
                self.state_stack.append(action)
                self.stack.push(next_token)
                self.input_buffer.pop(0)

            elif action < 0:
                # Reduce operation
                production_index = -action
                production = _lr_productions[production_index]
                lhs, rhs = production[0].split(' -> ')
                rhs = rhs.split(' ')
                rhs_len = len(rhs)

                children = []
                for _ in range(rhs_len):
                    self.state_stack.pop()
                    children.append(self.stack.pop())
                children = children[::-1]

                # Create an AST node based on the production
                if lhs == 'program':
                    # program -> expr SEMICOLON
                    ast_node = ProgramNode(children[0])
                elif lhs == 'expr':
                    if len(children) == 3:
                        # expr -> expr ADD term | expr SUBTRACT term
                        ast_node = BinaryOpNode(children[0], children[1].value, children[2])
                    else:
                        # expr -> term
                        ast_node = children[0]
                elif lhs == 'term':
                    if len(children) == 3:
                        # term -> term MULT factor | term DIVIDE factor
                        ast_node = BinaryOpNode(children[0], children[1].value, children[2])
                    else:
                        # term -> factor
                        ast_node = children[0]
                elif lhs == 'factor':
                    if len(children) == 3:
                        # factor -> LPAREN expr RPAREN
                        ast_node = ParenExprNode(children[1])
                    else:
                        # factor -> IDENTIFIER
                        ast_node = IdentifierNode(children[0].value)
                else:
                    # Default case: create a generic node
                    ast_node = ASTNode()

                self.stack.push(ast_node)
                # Perform the goto operation
                goto_state = _lr_goto[self.state_stack[-1]][lhs]
                self.state_stack.append(goto_state)

            elif action == 0:
                # Accept action
                print("Input successfully parsed!")
                ast_root = self.stack.pop()
                return ast_root

            else:
                print("Error: Invalid action encountered")
                break