import pyfol.types.basics as pf
import pyfol.prover.prover as pr
import pyfol.env.environment as env

if __name__ == "__main__":
    env = env.ProofEnvironment() # Define um ambiente de prova.
    prover = pr.AutomatedProver(env)

    # Define uma nova constante ao ambiente.
    a, b, c = env.addConst(name="a"), env.addConst(name="b"), env.addConst(name="c")

    # Define novos predicados.
    P = env.addPred(name="P", num_args=3)
    P1, P2, P3 = env.addPred(name="P1", num_args=1), env.addPred(name="P2", num_args=1), env.addPred(name="P3", num_args=1)
    P33 = env.addPred(name="P33", num_args=1)
    Q, Q1, Q0 = env.addPred(name="Q", num_args=1), env.addPred(name="Q1", num_args=1), env.addPred(name="Q0", num_args=1)
    R = env.addPred(name="R", num_args=1)
    S, S0 = env.addPred(name="S", num_args=1), env.addPred(name="S0", num_args=1)
    T, T1 = env.addPred(name="T", num_args=1), env.addPred(name="T1", num_args=1)

    # Supõe uma proposição.
    env.sup(P.apply(pf.params([env.x(1),env.x(2),env.x(3)])) >> Q.apply(pf.params([env.x(1)])))
    env.sup(P.apply(pf.params([env.x(1),env.x(2),env.x(3)])) >> Q.apply(pf.params([env.x(2)])))
    env.sup(P.apply(pf.params([env.x(1),env.x(2),env.x(3)])) >> ~Q.apply(pf.params([env.x(3)])))
    env.sup(P.apply(pf.params([env.x(1),env.x(2),env.x(3)])) >> R.apply(pf.params([env.x(1), env.x(2)])))
    env.sup(P.apply(pf.params([env.x(1),env.x(2),env.x(3)])) >> S.apply(pf.params([env.x(3), env.x(2)])))

    env.sup(Q.apply(pf.params([env.x(1)])) >> ~T.apply(pf.params([env.x(1)])))
    env.sup(Q.apply(pf.params([env.x(1)])) >> Q0.apply(pf.params([env.x(1)])))

    env.sup(R.apply(pf.params([env.x(1),env.x(2)])) >> R.apply(pf.params([env.x(2), env.x(1)])))
    env.sup(R.apply(pf.params([env.x(1),env.x(2)])) >> ~T.apply(pf.params([env.x(1)])))

    env.sup(S.apply(pf.params([env.x(1),env.x(2)])) >> ~T.apply(pf.params([env.x(2)])))
    env.sup(S.apply(pf.params([env.x(1),env.x(2)])) >> S0.apply(pf.params([env.x(1)])))
    env.sup(S.apply(pf.params([env.x(1),env.x(2)])) >> S0.apply(pf.params([env.x(2)])))

    env.sup(~T.apply(pf.params([env.x(1)])) >> T1.apply(pf.params([env.x(1)])))

    # env.inf_rules.print()
    # print()
    # env.graph.print()

    # Supõe um predicado: Homem(x) => Mortal(x)
    env.sup(P.apply(pf.params([a,b,c])))

    # Provar.
    prover.prove(~T.apply(pf.params([b])))

    # env.sup(~T.apply(pf.params([env.x(1)])) >> ~P1.apply(pf.params([env.x(1)])))
    # env.sup(S.apply(pf.params([env.x(1), env.x(2)])) >> P1.apply(pf.params([env.x(1)])))
    # env.sup(R.apply(pf.params([env.x(1), env.x(2)])) >> P3.apply(pf.params([env.x(2)])))

    # env.sup(~P1.apply(pf.params([env.x(1)])) >> P2.apply(pf.params([env.x(1)])))
    # env.sup(P3.apply(pf.params([env.x(1)])) >> P2.apply(pf.params([env.x(1)])))

    # env.sup(~P1.apply(pf.params([env.x(1)])) >> Q1.apply(pf.params([env.x(1)])))
    # env.sup(P2.apply(pf.params([env.x(1)])) >> Q1.apply(pf.params([env.x(1)])))
    # env.sup(P3.apply(pf.params([env.x(1)])) >> Q1.apply(pf.params([env.x(1)])))
    # env.sup(P3.apply(pf.params([env.x(1)])) >> P33.apply(pf.params([env.x(1)])))

    # prover.prove(Q1.apply(pf.params([b])))