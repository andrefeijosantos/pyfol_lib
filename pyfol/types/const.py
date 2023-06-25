class Const:
    def __init__(self, _name):
        self.name = _name

    def __repr__(self):
        return f"<pyfol.Const {self.name}>"
    
    def __eq__(self, other):
        return self.name == other.name