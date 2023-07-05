import pyfol.prover.prover as pr
import pyfol.env.environment as env

import pyfol.ds.graph_drawer as gd

if __name__ == "__main__":
    # Define um ambiente de prova.
    env = env.ProofEnvironment() 

    # Define uma nova constante ao ambiente.
    x = env.addConst(name="x")

    # Define novos predicados.
    P,P1,P2  = env.addPred(name="P", num_args=1),env.addPred(name="P1", num_args=1),env.addPred(name="P2", num_args=1)
    P3,P4,P5  = env.addPred(name="P3", num_args=1),env.addPred(name="P4", num_args=1),env.addPred(name="P5", num_args=1)
    Q = env.addPred(name="Q", num_args=1)
    T = env.addPred(name="T", num_args=1)
    S = env.addPred(name="S", num_args=1)
    S1 = env.addPred(name="S1", num_args=1)
    S2 = env.addPred(name="S2", num_args=1)
    S3 = env.addPred(name="S3", num_args=1)
    R = env.addPred(name="R", num_args=1)

    # Supõe uma proposição.
    env.sup(R.apply([x]))

    env.sup(~P.apply([env.x(1)]) >> P1.apply([env.x(1)]))
    env.sup(~P.apply([env.x(1)]) >> P2.apply([env.x(1)]))
    env.sup(~P.apply([env.x(1)]) >> P3.apply([env.x(1)]))
    env.sup(~P.apply([env.x(1)]) >> P4.apply([env.x(1)]))
    env.sup(~P.apply([env.x(1)]) >> P5.apply([env.x(1)]))

    env.sup(R.apply([env.x(1)]) >> T.apply([env.x(1)]))
    env.sup(R.apply([env.x(1)]) >> S3.apply([env.x(1)]))
    env.sup(S3.apply([env.x(1)]) >> S2.apply([env.x(1)]))
    env.sup(S2.apply([env.x(1)]) >> S1.apply([env.x(1)]))
    env.sup(S1.apply([env.x(1)]) >> Q.apply([env.x(1)]))
    env.sup(Q.apply([env.x(1)]) >> P.apply([env.x(1)]))
    env.sup(T.apply([env.x(1)]) >> P.apply([env.x(1)]))

    # Provar.
    env.prove(pr.Proof(P.apply([x]), _verbose=False))

    # Desenha o grafo.
    g = gd.GraphDrawer(env)
    g.draw()