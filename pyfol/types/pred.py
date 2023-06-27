from pyfol.logical_operators.logical_or import *
from pyfol.logical_operators.logical_and import *
from pyfol.types.temp_pred import TempPred
from pyfol.types.prop import Prop
from pyfol.types.user_const import UserConst

class Pred:
    def __init__(self, _name, _num_args, _id):
        self.name     = _name
        self.num_args = _num_args
        self.string   = None
        self.id       = _id

    def apply(self, params):
        if all(isinstance(p, UserConst) for p in params): 
            return Prop(self, params)
        else:
            return TempPred(self, params, True)

    def getId(self):
        return self.id

    def getString(self):
        self.string = f"<pyfol.Pred{self.num_args} {self.name}>"
        return self.string

    def __repr__(self):
        if self.string != None:
            return self.string
        return self.getString()

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

    def __eq__(self, other):
        return self.name == other.name and self.num_args == other.num_args
    