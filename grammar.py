

class Grammar:
    """C Grammar written by ChatGPT"""
    def __init__(self):
        # Define terminals (tokens)
        self.tokens = [
            "IDENTIFIER", "CONSTANT", "STRING_LITERAL", "TYPE",
            "OPERATOR", "REL_OP", "ASSIGN_OP", "SEMI", "COMMA",
            "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LSQUARE", "RSQUARE",
            "RETURN", "IF", "ELSE", "WHILE", "FOR"
        ]

        # Define non-terminals
        self.non_terminals = [
            "program", "declaration_list", "declaration", "var_declaration",
            "func_declaration", "param_list", "param", "statement",
            "expr_stmt", "compound_stmt", "local_declarations",
            "statement_list", "selection_stmt", "iteration_stmt",
            "return_stmt", "expression", "assignment_expr",
            "logical_or_expr", "logical_and_expr", "equality_expr",
            "relational_expr", "additive_expr", "term", "factor",
            "function_call", "arg_list"
        ]

        # Grammar rules (productions)
        self.rules = {
            "program": [["declaration_list"]],
            "declaration_list": [
                ["declaration_list", "declaration"],
                ["declaration"]
            ],
            "declaration": [
                ["var_declaration"],
                ["func_declaration"]
            ],
            "var_declaration": [
                ["TYPE", "IDENTIFIER", "SEMI"],
                ["TYPE", "IDENTIFIER", "LSQUARE", "CONSTANT", "RSQUARE", "SEMI"]
            ],
            "func_declaration": [
                ["TYPE", "IDENTIFIER", "LPAREN", "param_list", "RPAREN", "compound_stmt"],
                ["TYPE", "IDENTIFIER", "LPAREN", "RPAREN", "compound_stmt"]
            ],
            "param_list": [
                ["param_list", "COMMA", "param"],
                ["param"]
            ],
            "param": [
                ["TYPE", "IDENTIFIER"]
            ],
            "statement": [
                ["expr_stmt"],
                ["compound_stmt"],
                ["selection_stmt"],
                ["iteration_stmt"],
                ["return_stmt"]
            ],
            "expr_stmt": [
                ["expression", "SEMI"],
                ["SEMI"]
            ],
            "compound_stmt": [
                ["LBRACE", "local_declarations", "statement_list", "RBRACE"],
                ["LBRACE", "RBRACE"]
            ],
            "local_declarations": [
                ["local_declarations", "var_declaration"],
                []
            ],
            "statement_list": [
                ["statement_list", "statement"],
                []
            ],
            "selection_stmt": [
                ["IF", "LPAREN", "expression", "RPAREN", "statement"],
                ["IF", "LPAREN", "expression", "RPAREN", "statement", "ELSE", "statement"]
            ],
            "iteration_stmt": [
                ["WHILE", "LPAREN", "expression", "RPAREN", "statement"],
                ["FOR", "LPAREN", "expr_stmt", "expr_stmt", "RPAREN", "statement"],
                ["FOR", "LPAREN", "expr_stmt", "expr_stmt", "expression", "RPAREN", "statement"]
            ],
            "return_stmt": [
                ["RETURN", "SEMI"],
                ["RETURN", "expression", "SEMI"]
            ],
            "expression": [
                ["assignment_expr"]
            ],
            "assignment_expr": [
                ["IDENTIFIER", "ASSIGN_OP", "expression"],
                ["logical_or_expr"]
            ],
            "logical_or_expr": [
                ["logical_or_expr", "||", "logical_and_expr"],
                ["logical_and_expr"]
            ],
            "logical_and_expr": [
                ["logical_and_expr", "&&", "equality_expr"],
                ["equality_expr"]
            ],
            "equality_expr": [
                ["equality_expr", "REL_OP", "relational_expr"],
                ["relational_expr"]
            ],
            "relational_expr": [
                ["relational_expr", "REL_OP", "additive_expr"],
                ["additive_expr"]
            ],
            "additive_expr": [
                ["additive_expr", "OPERATOR", "term"],
                ["term"]
            ],
            "term": [
                ["term", "OPERATOR", "factor"],
                ["factor"]
            ],
            "factor": [
                ["LPAREN", "expression", "RPAREN"],
                ["IDENTIFIER"],
                ["CONSTANT"],
                ["STRING_LITERAL"]
            ],
            "function_call": [
                ["IDENTIFIER", "LPAREN", "arg_list", "RPAREN"],
                ["IDENTIFIER", "LPAREN", "RPAREN"]
            ],
            "arg_list": [
                ["arg_list", "COMMA", "expression"],
                ["expression"]
            ]
        }

    def get_rules(self):
        return self.rules

    def get_tokens(self):
        return self.tokens

    def get_non_terminals(self):
        return self.non_terminals
