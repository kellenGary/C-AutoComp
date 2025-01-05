class Production:
    """Class for production rule made for use in parsingTable.py"""
    def __init__(self, lhs, rhs, lookahead=None):
        self.lhs = lhs
        self.rhs = rhs
        self.dot = 0
        self.lookahead = lookahead

    def __repr__(self):
        """Returns a string representation"""
        rhs_str = " ".join(str(item) for item in self.rhs)
        return f"{self.lhs} -> {rhs_str}"

    def advance_dot(self):
        """Advance the dot by one position"""
        if self.dot < len(self.rhs):
            self.dot += 1

    def __eq__(self, other):
        """Check if two productions are equal"""
        return (self.lhs == other.lhs and
                self.rhs == other.rhs and
                self.dot == other.dot and
                self.lookahead == other.lookahead)

    def __hash__(self):
        """Make the Production class hashable"""
        rhs_tuple = tuple(tuple(item) if isinstance(item, list) else item for item in self.rhs)
        lookahead_hashable = tuple(self.lookahead) if self.lookahead else ()
        return hash((self.lhs, rhs_tuple, self.dot, lookahead_hashable))
