import re
from enum import Enum

class TokenType(Enum):
    IDENTIFIER = 'IDENTIFIER'
    SEMICOLON = 'SEMICOLON'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    ADD = "ADD"
    SUBTRACT = 'SUBTRACT'
    MULT = 'MULT'
    DIVIDE = 'DIVIDE'


operators = ['+', '-', '*', '/']
punctuations = [';', '(', ')']
punctuationString = ['SEMICOLON', 'LPAREN', 'RPAREN']

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __hash__(self):
        return hash((self.type, self.value))


class Tokenizer:
    def __init__(self, input_file_path):
        self.file = open(input_file_path, 'r')
        self.tokens = []
        self.SEPARATORS = '\t\n\r'

    def isOperator(self, word):
        return word in operators

    def isPunctuation(self, token):
        """Check if the token is a punctuation mark."""
        return token in punctuations

    def getOperatorType(self, word):
        if word == '+':
            return TokenType.ADD.value
        elif word == '-':
            return TokenType.SUBTRACT.value
        elif word == '*':
            return TokenType.MULT.value
        elif word == '/':
            return TokenType.DIVIDE.value

    def tokenize(self):
        lines = self.file.read().split('\n')
        for line in lines:
            words = re.split('(\W)', line.strip())
            i = 0
            while i < len(words):
                word = words[i]

                if not word:
                    i += 1
                    continue

                if word.isdigit():
                    token = Token(TokenType.IDENTIFIER.value, word)
                    self.tokens.append(token)
                elif self.isOperator(word):
                    token = Token(self.getOperatorType(word), word)
                    self.tokens.append(token)
                elif self.isPunctuation(word):
                    token = Token(TokenType.__dict__.get(punctuationString[punctuations.index(word)], 'UNKNOWN').value, word)
                    self.tokens.append(token)

                i += 1

    def getTokens(self):
        return self.tokens

    def printTokens(self):
        for token in self.tokens:
            print(f'{token.type}, {token.value}')