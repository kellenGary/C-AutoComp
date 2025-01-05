from production import Production


class ParsingTable:
    def __init__(self, grammar):
        self.grammar = grammar
        self.states = []
        self.transitions = {}
        self.build_states_and_transitions()

    def constructParsingTable(self):
        action = {}
        goto = {}
        for state_index, state in enumerate(self.states):
            for item in state:
                # Shift
                if item.dot < len(item.rhs):
                    symbol = item.rhs[item.dot]
                    if symbol in self.grammar.terminals:
                        action[(state_index, symbol)] = ('shift', self.transitions[(state_index, symbol)])

                # Reduce
                elif item.dot == len(item.rhs):
                    if item.lhs != self.grammar.start_symbol:
                        for lookahead in [item.lookahead]:
                            action[(state_index, lookahead)] = ('reduce', item.lhs, item.rhs)

            # Accept
            if any(item.lhs == self.grammar.start_symbol and item.dot == len(item.rhs) for item in state):
                action[(state_index, "$")] = ("accept",)

            for symbol in self.grammar.non_terminals:
                if (state_index, symbol) in self.transitions:
                    goto[(state_index, symbol)] = self.transitions[(state_index, symbol)]

        return action, goto

    def closure(self, items):
        """Closure function to compute the closure of a set of items"""
        closure_items = set(items)
        while True:
            new_items = set(closure_items)
            for item in closure_items:
                if item.dot < len(item.rhs):
                    symbol = item.rhs[item.dot]
                    if symbol in self.grammar.non_terminals:
                        for production in self.grammar.get_rules_for(symbol):
                            rhs_tuple = tuple(production[1])
                            new_items.add(Production(symbol, rhs_tuple, item.lookahead))
            if len(new_items) == len(closure_items):
                break
            closure_items = new_items
        return closure_items

    def transition(self, items, symbol):
        """Transition function to get a transition in a set of items"""
        next_items = set()
        for item in items:
            if item.dot < len(item.rhs) and item.rhs[item.dot] == symbol:
                sym_l = [item.rhs[:item.dot], [symbol], item.rhs[item.dot + 1:]]
                next_item = Production(item.lhs, sym_l, item.lookahead)
                next_items.add(next_item)
        return next_items

    def build_states_and_transitions(self):
        """Build states and transitions from the grammar"""
        initial_item = Production("S'", ["program"], "$")
        initial_state = self.closure([initial_item])
        self.states.append(initial_state)

        state_index = 0
        while state_index < len(self.states):
            state = self.states[state_index]
            for symbol in self.grammar.terminals.union(self.grammar.non_terminals):
                next_state = self.transition(state, symbol)
                if next_state:
                    if next_state not in self.states:
                        self.states.append(next_state)
                    self.transitions[(state_index, symbol)] = self.states.index(next_state)
            state_index += 1
