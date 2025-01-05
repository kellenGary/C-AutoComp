from stack import Stack
from grammar import Grammar
from parsingTable import ParsingTable


class Parser:
    """LR(1) PARSER"""
    def __init__(self, tokens):
        self.stack = Stack()
        self.grammar = Grammar()
        self.tokens = tokens
        self.parsingTable = ParsingTable(self.grammar)

    def parse(self):
        actions = self.parsingTable.actions
        goto = self.parsingTable.goto

        for rule in self.grammar.rules:
            print(rule[1])

        i = 0
        while i < len(self.tokens):
            token = self.tokens[i]
            token_tuple = tuple([0, token.type])
            print(token.type)

            if actions.get(token_tuple):
                # Action functions for terminal functions
                action_tuple = actions.get(token_tuple)
                action = action_tuple[0]

                if action == 'shift':
                    shift = action_tuple[1]
                    self.stack.push(token)
                    self.stack.push(self.tokens[i:int(shift)])
                elif action == 'reduce':
                    rule = action_tuple[1]
                    while not rule.startswith(self.stack.head):
                        self.stack.pop()
                elif action == 'accept':
                    print('the token was parsed.')

            elif goto.get(token_tuple):
                # Goto function for non-terminals
                print('goto')
            else:
                # Error so we need to call AI to fix the tokens
                # print('something went wrong')
                y = 1
            i += 1

    def computeFirst(self):
        first = {symbol: set() for symbol in self.grammar.rules}

        def findFirst(symbol):
            if symbol not in self.grammar.rules:
                return {symbol}
            if first[symbol]:
                return first[symbol]
            for production in self.grammar.rules[symbol]:
                for sym in production:
                    first[symbol] |= findFirst(sym) - {'ε'}
                    if "ε" not in findFirst(sym):
                        break
                else:
                    first[symbol].add('ε')
            return first[symbol]

        for nonterminal in self.grammar.rules:
            findFirst(nonterminal)
        return first
