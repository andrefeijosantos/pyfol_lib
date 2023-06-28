class ProofData:
    def __init__(self, _proved, _prop, _rntm, _eps, _proved_eps, _nodes):
        self.proved = _proved
        self.prop = _prop
        self.rntm = _rntm
        self.eps = _eps
        self.proved_eps = _proved_eps
        self.total_nodes = _nodes

    def __getitem__(self, item):
        return (self.proved, self.prop, self.rntm, self.eps, self.proved_eps, self.total_nodes)[item]