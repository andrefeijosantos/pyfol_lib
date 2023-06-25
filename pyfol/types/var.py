class Var:
    def __init__(self, _name):
        self.name = _name

    def __repr__(self):
        return f"<pyfol.Var {self.name}>"

    def __hash__(self):
        total = 0
        for i in range(len(self.name)):
            total += 2**(len(self.name)-i) * ord(self.name[i])
        return total

    def __eq__(self, other):
        return self.name == other.name