from stack import Stack
from parsetab import _lr_action, _lr_goto, _lr_productions
from tokenizer import Token
from ErrorRecovery import fixTokens

class Parser:
    """LR(1) PARSER"""
    def __init__(self):
        self.stack = Stack()
        self.state_stack = [0]
        self.input_buffer = []

    def parse(self, tokens):
        self.input_buffer = tokens + [Token('$end', None)]

        while True:
            current_state = self.state_stack[-1]
            next_token = self.input_buffer[0]
            next_type = next_token.type

            if next_type not in _lr_action[current_state]:
                print(self.stack, next_type)
                fixTokens(self.stack, next_token)
                break

            action = _lr_action[current_state][next_type]

            if action > 0:
                # print(f"Shift: {next_token}")
                self.state_stack.append(action)
                self.stack.push(next_token)
                self.input_buffer.pop(0)

            elif action < 0:
                production_index = -action
                production = _lr_productions[production_index]
                lhs, rhs = production[0].split(' -> ')
                rhs = rhs.split(' ')
                rhs_len = len(rhs)

                # print(f"Reduce: {lhs} -> {''.join(rhs)}")

                for _ in range(rhs_len):
                    self.state_stack.pop()
                    self.stack.pop()

                self.stack.push(Token(lhs, None))
                goto_state = _lr_goto[self.state_stack[-1]][lhs]
                self.state_stack.append(goto_state)

            elif action == 0:
                print("Input successfully parsed!")
                return

