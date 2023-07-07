from pyfol.types.prop import Prop
from pyfol.types.temp_prop import TempProp

class Proof:
    def __init__(self, _prop, _verbose=True):
        if isinstance(_prop, Prop):
            self.prop_to_prove_1 = TempProp(_prop, False)
        elif isinstance(_prop, TempProp):
            self.prop_to_prove_1 = _prop
            self.prop_to_prove_1.hyp = ~self.prop_to_prove_1.hyp
        self.verbose = _verbose