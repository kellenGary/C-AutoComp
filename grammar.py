class Grammar:
    def __init__(self):
        self.rules = []  # Stores rules as tuples: (LHS, RHS)
        self.non_terminals = set()
        self.terminals = set()
        self.start_symbol = None
        self.buildGrammar()

    def add_rule(self, lhs, rhs):
        """
        Add a production.py rule to the grammar.
        Args:
            lhs (str): The left-hand side of the rule (a non-terminal).
            rhs (list): The right-hand side of the rule (list of terminals/non-terminals).
        """
        if not self.start_symbol:
            self.start_symbol = lhs  # First added rule defines the start symbol

        self.rules.append((lhs, rhs))
        self.non_terminals.add(lhs)
        for symbol in rhs:
            if symbol.islower() or symbol.isdigit() or symbol in ['(', ')', ',', ';', '=', '+', '-', '*', '/']:
                self.terminals.add(symbol)

    def get_rules_for(self, non_terminal):
        """
        Retrieve all rules for a given non-terminal.
        Args:
            non_terminal (str): The non-terminal to retrieve rules for.
        Returns:
            list: Rules with the given non-terminal as LHS.
        """
        return [rule for rule in self.rules if rule[0] == non_terminal]

    def __str__(self):
        """
        Returns a string representation of the grammar.
        """
        grammar_str = "Grammar:\n"
        for lhs, rhs in self.rules:
            grammar_str += f"{lhs} → {' '.join(rhs)}\n"
        return grammar_str
    
    def buildGrammar(self):
        # Add grammar rules for C

        # Augmented rule for LR(1) parser
        self.add_rule("S'", ["program"])

        # Start with the program
        self.add_rule("program", ["external_declaration", "program"])
        self.add_rule("program", ["external_declaration"])
        
        # External declarations
        self.add_rule("external_declaration", ["function_definition"])
        self.add_rule("external_declaration", ["declaration"])
        
        # Function definitions
        self.add_rule("function_definition", ["type_specifier", "IDENTIFIER", "(", "parameter_list", ")", "compound_statement"])
        self.add_rule("function_definition", ["type_specifier", "IDENTIFIER", "(", ")", "compound_statement"])
        
        # Parameter list
        self.add_rule("parameter_list", ["parameter_declaration"])
        self.add_rule("parameter_list", ["parameter_list", ",", "parameter_declaration"])
        
        self.add_rule("parameter_declaration", ["type_specifier", "IDENTIFIER"])
        
        # Declarations
        self.add_rule("declaration", ["storage_class_specifier", "type_specifier", "init_declarator_list", ";"])
        self.add_rule("declaration", ["type_specifier", "init_declarator_list", ";"])
        self.add_rule("declaration", ["type_specifier", ";"])
        
        # Init declarator list
        self.add_rule("init_declarator_list", ["init_declarator"])
        self.add_rule("init_declarator_list", ["init_declarator_list", ",", "init_declarator"])
        
        self.add_rule("init_declarator", ["IDENTIFIER"])
        self.add_rule("init_declarator", ["IDENTIFIER", "=", "initializer"])
        
        self.add_rule("initializer", ["expression"])
        
        # Storage class specifiers
        storage_classes = ["auto", "register", "static", "extern", "typedef"]
        for sc in storage_classes:
            self.add_rule("storage_class_specifier", [sc])
        
        # Type specifiers
        type_specifiers = ["int", "float", "double", "char", "void", "long", "short", "signed", "unsigned"]
        for ts in type_specifiers:
            self.add_rule("type_specifier", [ts])
        self.add_rule("type_specifier", ["struct", "IDENTIFIER"])
        self.add_rule("type_specifier", ["union", "IDENTIFIER"])
        self.add_rule("type_specifier", ["enum", "IDENTIFIER"])
        
        # Compound statement
        self.add_rule("compound_statement", ["{", "block_item_list", "}"])
        self.add_rule("block_item_list", ["block_item"])
        self.add_rule("block_item_list", ["block_item_list", "block_item"])
        self.add_rule("block_item", ["statement"])
        self.add_rule("block_item", ["declaration"])
        
        # Statements
        self.add_rule("statement", ["expression_statement"])
        self.add_rule("statement", ["compound_statement"])
        self.add_rule("statement", ["selection_statement"])
        self.add_rule("statement", ["iteration_statement"])
        self.add_rule("statement", ["jump_statement"])
        
        # Expression statement
        self.add_rule("expression_statement", ["expression", ";"])
        self.add_rule("expression_statement", [";"])
        
        # Selection statements
        self.add_rule("selection_statement", ["if", "(", "expression", ")", "statement"])
        self.add_rule("selection_statement", ["if", "(", "expression", ")", "statement", "else", "statement"])
        self.add_rule("selection_statement", ["switch", "(", "expression", ")", "statement"])
        
        # Iteration statements
        self.add_rule("iteration_statement", ["while", "(", "expression", ")", "statement"])
        self.add_rule("iteration_statement", ["do", "statement", "while", "(", "expression", ")", ";"])
        self.add_rule("iteration_statement", ["for", "(", "expression_statement", "expression_statement", ")", "statement"])
        self.add_rule("iteration_statement", ["for", "(", "expression_statement", "expression_statement", "expression", ")", "statement"])
        
        # Jump statements
        self.add_rule("jump_statement", ["goto", "IDENTIFIER", ";"])
        self.add_rule("jump_statement", ["continue", ";"])
        self.add_rule("jump_statement", ["break", ";"])
        self.add_rule("jump_statement", ["return", "expression", ";"])
        self.add_rule("jump_statement", ["return", ";"])
        
        # Expressions
        self.add_rule("expression", ["assignment_expression"])
        self.add_rule("expression", ["expression", ",", "assignment_expression"])
        
        self.add_rule("assignment_expression", ["IDENTIFIER", "=", "assignment_expression"])
        self.add_rule("assignment_expression", ["logical_or_expression"])
        
        # Logical expressions (and so on for all operators)
        self.add_rule("logical_or_expression", ["logical_and_expression"])
        self.add_rule("logical_or_expression", ["logical_or_expression", "||", "logical_and_expression"])

