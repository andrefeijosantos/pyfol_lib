from pyfol.types.var import Var

class ExistsPred:
    def __init__(self, _pred, _consts):
        self.pred   = _pred
        self.consts = [Const(x) for x in _consts]
        self.string = self.getString()

    def getString(self):
        self.string = f"<pyfol.ForAllPred {self.pred.name}("

        for i in range(len(self.vars)-1):
            self.string += self.vars[i].name + ","
        self.string += self.vars[len(self.vars)-1].name + ")>"

        return self.string

    def __repr__(self):
        return self.string

    def __or__(self, other):
        if isinstance(other, TempPred):
            return LogicalOR(TempPred(self, True), other)
        elif isinstance(other, Pred):
            return LogicalOR(TempPred(self, True), TempPred(other, True))

    def __and__(self, other):
        if isinstance(other, TempPred):
            return LogicalAND(TempPred(self, True), other)
        elif isinstance(other, Pred):
            return LogicalAND(TempPred(self, True), TempPred(other, True))

    def __invert__(self):
        return TempPred(self, False)
    