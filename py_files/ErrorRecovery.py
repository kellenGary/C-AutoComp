import os

from google import genai
from tokenizer import Token
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=api_key)
grammar = ("program -> expr SEMICOLON; "
           "expr -> expr ADD term | expr SUBTRACT term | term; "
           "term -> term MULT factor | term DIVIDE factor | factor; "
           "factor -> IDENTIFIER | LPAREN expr RPAREN")


def fixTokens(token_stack, invalid_tokens, copied_buffer, error_location):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=
        f"Fix the following unexpected token: {invalid_tokens.type, invalid_tokens.value}, within the state_stack:"
        f"{token_stack} using the grammar: {grammar} so the program compiles. "
        f"don't print anything extra. just the needed token type and token value to fix it with "
        f"the form 'token.type, token.value'"
    )
    # AI creates a string in format "type, value"
    token_info = response.text.split(', ')
    # Add the necessary token to the new token array
    return Token(token_info[0], token_info[1].replace('\n', ''))
