import ply.yacc as yacc

# Tokens used in the grammar
tokens = [
    "IDENTIFIER",
    "SEMICOLON", "LPAREN", "RPAREN", "ADD", "SUBTRACT", "MULT", "DIVIDE"
]

# Define grammar rules (no actual parsing logic needed)
def p_program(p):
    """program : expr SEMICOLON"""
    pass

def p_expr_add(p):
    """expr : expr ADD term"""
    pass

def p_expr_subtract(p):
    """expr : expr SUBTRACT term"""
    pass

def p_expr_term(p):
    """expr : term"""
    pass

def p_term_mult(p):
    """term : term MULT factor"""
    pass

def p_term_divide(p):
    """term : term DIVIDE factor"""
    pass

def p_term_factor(p):
    """term : factor"""
    pass

def p_factor_identifier(p):
    """factor : IDENTIFIER"""
    pass

def p_factor_group(p):
    """factor : LPAREN expr RPAREN"""
    pass

def p_error(p):
    """Handle parsing errors."""
    print(f"Syntax error at '{p.value}'")

# Create the parser (generate parsing table)
yacc.yacc(write_tables=True, debug=True)
