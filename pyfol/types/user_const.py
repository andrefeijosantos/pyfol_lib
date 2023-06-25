class UserConst:
    def __init__(self, _name, _id):
        self.name = _name
        self.id   = _id

    def __repr__(self):
        return f"<pyfol.UserConst {self.name}>"
    
    def getId(self):
        return self.id