from enum import Enum
import re

keywords = ['auto', 'const', 'double', 'float', 'int',
            'short', 'struct', 'unsigned', 'break', 'continue',
            'else', 'for', 'long', 'signed', 'switch',
            'void', 'case', 'default', 'enum', 'goto',
            'register', 'sizeof', 'typedef', 'volatile', 'char',
            'do', 'extern', 'if', 'return', 'static', 'union', 'while'
            ]

identifier = re.compile(r"^[^\d\W]\w*\Z", re.UNICODE)

operators = ['+', '-', '*', '/', '%', '==', '!=', '<', '>', '=', '+=', '-=', '*=', '/=']
punctuations = [';', '{', '}', '(', ')', ',', '.', '->']
punctuationString = ['SEMI', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'COMMA', 'DOT', 'ARROW']


class TokenType(Enum):
    # Keywords
    AUTO = 'AUTO'
    CONST = 'CONST'
    INT = 'INT'
    FLOAT = 'FLOAT'
    CHAR = 'CHAR'
    RETURN = 'RETURN'
    IF = 'IF'
    ELSE = 'ELSE'
    WHILE = 'WHILE'
    FOR = 'FOR'
    SWITCH = 'SWITCH'
    CASE = 'CASE'
    DEFAULT = 'DEFAULT'
    BREAK = 'BREAK'
    CONTINUE = 'CONTINUE'
    GOTO = 'GOTO'
    STATIC = 'STATIC'
    EXTERN = 'EXTERN'
    REGISTER = 'REGISTER'
    TYPEDEF = 'TYPEDEF'
    VOLATILE = 'VOLATILE'
    SIZEOF = 'SIZEOF'

    # Identifiers
    IDENTIFIER = 'IDENTIFIER'

    # Literals
    CONSTANT = 'CONSTANT'  # Integer or Floating-point literals
    STRING_LITERAL = 'STRING_LITERAL'
    CHARACTER_LITERAL = 'CHARACTER_LITERAL'
    FLOAT_LITERAL = 'FLOAT_LITERAL'

    # Operators
    OPERATOR = 'OPERATOR'  # General category for all operators
    ASSIGN_OP = 'ASSIGN_OP'  # Assignment operators (=, +=, -=, *=, /=)
    REL_OP = 'REL_OP'  # Relational operators (==, !=, <, >, <=, >=)

    # Punctuation/Special Symbols
    LPAREN = '('  # '('
    RPAREN = ')'  # ')'
    LBRACE = 'LBRACE'  # '{'
    RBRACE = 'RBRACE'  # '}'
    LSQUARE = 'LSQUARE'  # '['
    RSQUARE = 'RSQUARE'  # ']'
    SEMI = 'SEMI'  # ';'
    COMMA = 'COMMA'  # ','
    DOT = 'DOT'  # '.'
    ARROW = 'ARROW'  # '->'

    # Comments
    SINGLE_LINE_COMMENT = 'SINGLE_LINE_COMMENT'
    MULTI_LINE_COMMENT = 'MULTI_LINE_COMMENT'

    # Miscellaneous
    TYPE_SPECIFIER = 'TYPE_SPECIFIER'  # e.g., int, float, char
    STORAGE_CLASS_SPECIFIER = 'STORAGE_CLASS_SPECIFIER'  # e.g., static, extern


class Token:
    def __init__(self, type, value):
        self.value = value
        self.type = type


class Tokenizer:
    def __init__(self, input_file_path):
        self.file = open(input_file_path, 'r')
        self.tokens = []
        self.SEPARATORS = '\t\n\r'

    def __isKeyword(self, token):
        """Checks if the token is a keyword"""
        return token in keywords

    def __isIdentifier(self, token):
        """Check if the token is an identifier."""
        return re.match(identifier, token)

    def __isOperator(self, token):
        """Check if the token is an operator."""
        return token in operators

    def __isPunctuation(self, token):
        """Check if the token is a punctuation mark."""
        return token in punctuations

    def __formatInput(self):
        text = self.file.read().strip()
        text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
        text = re.sub(r'//.*', '', text)
        lines = text.splitlines()
        return lines

    def tokenize(self):
        """Reads the input stream and outputs a valid queue of tokens"""
        lines = self.__formatInput()
        for line in lines:
            words = re.split('(\W)', line.strip())
            i = 0
            while i < len(words):
                word = words[i].strip()

                # If empty line
                if not word:
                    i += 1
                    continue

                # String Literals
                if word.startswith("\"") and word.endswith('\"'):
                    token = Token(TokenType.STRING_LITERAL.value, word)
                    self.tokens.append(token)

                # Char literals
                elif word.startswith("'") and word.endswith("'"):
                    token = Token(TokenType.CHARACTER_LITERAL.value, word)
                    self.tokens.append(token)

                # nums or constants
                elif word.isdigit():
                    token = Token(TokenType.CONSTANT.value, word)
                    self.tokens.append(token)

                # Keywords
                elif self.__isKeyword(word):
                    token = Token(TokenType.__dict__.get(word.upper(), 'UNKNOWN').value, word)
                    self.tokens.append(token)

                # Identifiers
                elif self.__isIdentifier(word):
                    token = Token(TokenType.IDENTIFIER.value, word)
                    self.tokens.append(token)

                # Operators
                elif self.__isOperator(word):
                    token = Token(TokenType.OPERATOR.value, word)
                    self.tokens.append(token)

                # Punctuation
                elif self.__isPunctuation(word):
                    token = Token(TokenType.__dict__.get(punctuationString[punctuations.index(word)], 'UNKNOWN').value, word)
                    self.tokens.append(token)

                i += 1

    def getTokens(self):
        """Returns the queue of tokens"""
        return self.tokens

    def printTokens(self, type):
        for token in self.tokens:
            if token.type != type:
                print(f'{token.type}, {token.value}')
