from pyfol.logical_operators.logical_or import *
from pyfol.logical_operators.logical_and import *

class TempProp:
    def __init__(self, _prop, _hyp):
        self.prop   = _prop
        self.hyp    = _hyp
        
        if self.hyp: self.hash = self.prop.hash
        else:        self.hash = -self.prop.hash

    def getHash(self):
        return self.hash
        
    def getStrId(self):
        if self.hyp:
            return self.prop.getStrId()
        else:
            return "~" + self.prop.getStrId()
    
    def toString(self):
        if self.hyp:
            return self.prop.toString()
        return "~" + self.prop.toString()

    def __repr__(self):
        if self.hyp:
            return f"{self.prop}".replace(".Prop", ".TempProp")
        return f"{self.prop}".replace(".Prop", ".TempProp NOT")

    def __or__(self, other):
        from pyfol.types.prop import Prop
        if isinstance(other, TempProp):
            return LogicalOR(self, other)
        elif isinstance(other, Prop):
            return LogicalOR(self, TempProp(other, True))

    def __and__(self, other):
        from pyfol.types.prop import Prop
        if isinstance(other, TempProp):
            return LogicalAND(self, other)
        elif isinstance(other, Prop):
            return LogicalAND(self, TempProp(other, True))

    def __invert__(self):
        return TempProp(self.prop, ~self.hyp) ### CORRIGIR ###

    # REPENSAR!!!!!!!!
    def __lt__(self, other):
        return self.getHash() < other.getHash()