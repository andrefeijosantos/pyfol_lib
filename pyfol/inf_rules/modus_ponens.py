class ModusPonens:
    def __init__(self, _pred1, _pred2):
        self.pred1 = _pred1
        self.pred2 = _pred2
        self.prop = ""

    def setProp(self, _prop):
        self.prop = _prop
        return self

    def __repr__(self):
        return f"Modus Ponens({self.pred1.name} -> {self.pred2.name}, {self.prop.toString()})"