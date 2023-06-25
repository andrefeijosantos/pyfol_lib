import pyfol.env.environment as pf
import pyfol.types.params as p
import pyfol.types.user_const as uc
import pyfol.types.const as c
import pyfol.types.var as v

def params(args):
    u_consts, consts, vars = False, False, False
    for arg in args:
        if isinstance(arg, v.Var): vars = True
        elif isinstance(arg, c.Const): consts = True
        else: u_consts = True

    if vars and consts: return p.Params(args, p.FORALL_EXISTS)
    elif vars: return p.Params(args, p.FORALL)
    elif consts: return p.Params(args, p.EXISTS)
    return p.Params(args, p.PROP)