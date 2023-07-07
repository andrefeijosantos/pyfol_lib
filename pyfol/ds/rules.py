from pyfol.types.prop import Prop
from pyfol.types.temp_prop import TempProp

from pyfol.inf_rules.modus_ponens import ModusPonens
from pyfol.inf_rules.modus_tollens import ModusTollens

class Rules():
    def __init__(self, _ids):
        self.table = dict()
        self.ids   = _ids
        self.moves = dict()   # Mapeia um par de predicados nas regras de inferências usadas.

    # Adiciona uma linha ao mapa de regras
    def add(self, pred_id, deduction, move):
        try: self.table[pred_id].append(deduction)
        except: self.table[pred_id] = [deduction]
        if move == 0:
            self.moves[(abs(pred_id), abs(deduction))] = ModusPonens(self.ids[abs(pred_id)],self.ids[abs(deduction)])
        elif move == 1:
            self.moves[(abs(pred_id), abs(deduction))] = ModusTollens(self.ids[abs(pred_id)],self.ids[abs(deduction)])

    def getVertice(self, pred):
        k1 = pred.getId() + 1
        if not pred.hyp: k1 *= -1
        return k1

    def print(self):
        print(self.table)

    # Retorna todas as deduções a partir da proposição prop
    def getDeductions(self, prop):
        pred_id = (prop.prop.pred.getId()+1)
        if not prop.hyp: pred_id *= -1

        deductions = []
        try:
            for ded in self.table[pred_id]:
                prop = self.ids[abs(ded)].apply(prop.prop.consts)
                if ded < 0: prop = ~prop
                else: prop = TempProp(prop, True)
                deductions.append(prop)
        except: pass

        return deductions