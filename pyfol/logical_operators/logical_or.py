from pyfol.inf_rules.modus_tollens import ModusTollens
from pyfol.inf_rules.modus_ponens import ModusPonens

class LogicalOR:
    def __init__(self, _temp1, _temp2):
        self.temp1 = _temp1
        self.temp2 = _temp2

    def apply(self, rules):
        k1 = rules.getVertice(~self.temp1)
        k2 = rules.getVertice(self.temp2)

        rules.add(k1, k2)
        rules.add(-k2, -k1)

    def __repr__(self):
        return f"{self.temp1} OR {self.temp2}"