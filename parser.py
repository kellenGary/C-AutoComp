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
