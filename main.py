import sys
from tokenizer import Tokenizer
from parser import Parser


def main():
    # Get input file from CLI
    arg_num = len(sys.argv)
    if arg_num > 2:
        print('ERROR: Too many arguments passed.')
        return 0
    input_file_path = sys.argv[1]

    tokenizer = Tokenizer(input_file_path)
    tokenizer.tokenize()
    tokenizer.printTokens(None)

    # tokens = tokenizer.getTokens()
    # parser = Parser(tokens)


if __name__ == "__main__":
    main()
