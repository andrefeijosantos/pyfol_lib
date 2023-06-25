from pyfol.logical_operators.logical_or import *
from pyfol.logical_operators.logical_and import *
from pyfol.types.temp_prop import TempProp

class Prop:
    def __init__(self, _pred, _consts):
        self.consts = _consts
        self.pred   = _pred
        self.string = self.toString()

        # Calcula o hash
        self.hash,p = 10000000000*(self.pred.id+1), len(self.consts)
        for const in self.consts: self.hash += 2**p * (const.id+1); p-=1

    def toString(self):
        self.string = self.pred.name + '('
        for i in range(len(self.consts)-1):
            self.string += self.consts[i].name + ","
        self.string += self.consts[len(self.consts)-1].name + ")"

        return self.string

    def getHash(self):
        return self.hash
    
    def getStrId(self):
        str_id = str(self.pred.getId())
        for const in self.consts: str_id += ";" + str(const.getId())
        return str_id

    def __repr__(self):
        return f"<Pyfol.Prop {self.string}>"

    def __or__(self, other):
        if isinstance(other, TempProp):
            return LogicalOR(TempProp(self, True), other)
        elif isinstance(other, Prop):
            return LogicalOR(TempProp(self, True), TempProp(other, True))

    def __and__(self, other):
        if isinstance(other, TempProp):
            return LogicalAND(TempProp(self, True), other)
        elif isinstance(other, Prop):
            return LogicalAND(TempProp(self, True), TempProp(other, True))

    def __invert__(self):
        return TempProp(self, False) ### CORRIGIR ###