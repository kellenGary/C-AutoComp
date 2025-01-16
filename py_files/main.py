import sys
from exprTokenizer import Tokenizer
import yaccTableBuilder
from parser import Parser


def main():
    # Get input file from CLI
    arg_num = len(sys.argv)
    if arg_num > 2:
        print('ERROR: Too many arguments passed.')
        return 0
    input_file_path = sys.argv[1]

    # Seems weird but this builds the Parsing Table using ply.yacc
    yaccTableBuilder

    tokenizer = Tokenizer(input_file_path)
    tokenizer.tokenize()

    parser = Parser()
    parser.parse(tokenizer.getTokens())

if __name__ == "__main__":
    main()
