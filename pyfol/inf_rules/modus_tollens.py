class ModusTollens:
    def __init__(self, _temp1, _temp2, _conv):
        self.temp1 = _temp1
        self.temp2 = ~_temp2
        self.convertion = _conv

    def apply(self, args, name=True):
        from pyfol.types.temp_prop import TempProp
        from pyfol.types.prop import Prop
        if name:
            return (TempProp(Prop(self.temp2.pred, self.convert(args, self.convertion)), self.temp1.hyp), self.toString(args))
        else:
            return TempProp(Prop(self.temp2.pred, self.convert(args, self.convertion)), self.temp1.hyp)

    def convert(self, consts, conversion):
        converted_consts = [None] * len(conversion)
        for i in range(len(conversion)):
            converted_consts[i] = consts[conversion[i]]
        return converted_consts

    def toString(self, args):
        string = f"2;{self.temp2.getId()};{self.temp1.getId()};"
        for arg in args: string += str(arg.id) + " "
        return string
    
    def __repr__(self):
        return str((self.temp1, self.temp2, self.convertion))