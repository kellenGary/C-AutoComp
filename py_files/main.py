import sys
import yaccTableBuilder
from exprTokenizer import Tokenizer
from parser import Parser
from codeGenerator import LLVMCodeGen
import linker


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
    ast = parser.parse(tokenizer.getTokens())

    code_gen = LLVMCodeGen()
    code_gen.compile(ast)
    code_gen.save_ir_to_file('testoutput.ll')
    linker.compile_and_link('testoutput.ll')

if __name__ == "__main__":
    main()
