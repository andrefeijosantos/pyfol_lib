import pyfol.types.basics as pf
from pyfol.types.prop import Prop
from pyfol.types.temp_prop import TempProp

class Rules():
    def __init__(self, _ids):
        self.table = dict()
        self.ids   = _ids

    def add(self, pred_id, deduction):
        try: self.table[pred_id].append(deduction)
        except: self.table[pred_id] = [deduction]

    def getVertice(self, pred):
        k1 = pred.getId() + 1
        if not pred.hyp: k1 *= -1
        return k1

    def print(self):
        print(self.table)

    def find(self, pred):
        print("oi")

    def getDeductions(self, prop):
        pred_id = (prop.prop.pred.getId()+1)
        if not prop.hyp: pred_id *= -1

        deductions = []
        try:
            for ded in self.table[pred_id]:
                prop = self.ids[abs(ded)].apply(pf.params(prop.prop.consts))
                if ded < 0: prop = ~prop
                else: prop = TempProp(prop, True)
                deductions.append(prop)
        except: pass

        return deductions