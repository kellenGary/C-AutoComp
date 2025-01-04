from stack import Stack
from grammar import Grammar
"""LR(1) PARSER"""


class Parser:

    def __init__(self, tokens):
        self.stack = Stack()
        self.grammar = Grammar()

    def parseTokens(self):
        while not self.stack.isEmpty():
            token = self.stack.pop()
            peek_node = self.stack.peek()

    def printStack(self):
            nodes = []
            for i in range(self.stack.getSize()):
                node = self.stack.pop()
                print(node.value)
            self.stack.append(nodes)
