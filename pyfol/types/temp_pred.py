from pyfol.logical_operators.logical_or import *
from pyfol.logical_operators.logical_and import *

class TempPred:
    def __init__(self, _pred, _params, _hyp):
        self.pred   = _pred
        self.params = _params
        self.hyp    = _hyp

    def apply(self, params):
        return self.pred.apply(params)

    def getId(self):
        return self.pred.getId()

    def __repr__(self):
        if self.hyp:
            return f"<pyfol.TempPred {self.pred.name}>"
        return f"<pyfol.TempPred NOT {self.pred.name}>"

    def __or__(self, other):
        return LogicalOR(self, other)

    def __eq__(self, other):
        return self.pred.id == other.pred.id and self.hyp == other.hyp

    def __and__(self, other):
        print("AND")

    def __invert__(self):
        return TempPred(self.pred, self.params, not self.hyp)

    def __rshift__(self, other):
        return ~self | other