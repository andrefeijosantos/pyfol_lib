PROP          = 1
FORALL        = 2
EXISTS        = 3
FORALL_EXISTS = 4

class Params:
    def __init__(self, _args, _tp):
        self.args = _args
        self.tp = _tp

    def typeToString(self):
        if self.tp == 1: return "PROP"
        elif self.tp == 2: return "FORALL"
        elif self.tp == 3: return "EXISTS"
        elif self.tp == 4: return "FORALL_EXISTS"

    def __repr__(self):
        return str(self.args)

    def __len__(self):
        return len(self.args)