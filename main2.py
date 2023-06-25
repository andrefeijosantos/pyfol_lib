import pyfol.types.basics as pf
import pyfol.prover.prover as pr
import pyfol.env.environment as env

import pyfol.ds.graph_drawer as gd

if __name__ == "__main__":
    env = env.ProofEnvironment() # Define um ambiente de prova.
    proof = pr.Proof(env, _verbose=False)

    # Define uma nova constante ao ambiente.
    socrates = env.addConst(name="Socrates")

    # Define novos predicados.
    homem  = env.addPred(name="Homem", num_args=1)
    animal  = env.addPred(name="Animal", num_args=1)
    mortal = env.addPred(name="Mortal", num_args=1)
    imortal = env.addPred(name="Imortal", num_args=1)
    irracional = env.addPred(name="Irracional", num_args=1)

    # Supõe uma proposição.
    env.sup(~irracional.apply(pf.params([socrates])))

    # Supõe um predicado: Homem(x) => Mortal(x)
    env.sup(homem.apply(pf.params([env.x(1)])) >> mortal.apply(pf.params([env.x(1)])))
    env.sup(~mortal.apply(pf.params([env.x(1)])) >> imortal.apply(pf.params([env.x(1)])))
    env.sup(imortal.apply(pf.params([env.x(1)])) >> ~mortal.apply(pf.params([env.x(1)])))
    env.sup(~homem.apply(pf.params([env.x(1)])) >> irracional.apply(pf.params([env.x(1)])))
    env.sup(~homem.apply(pf.params([env.x(1)])) >> animal.apply(pf.params([env.x(1)])))

    # Provar.
    proof.prove(mortal.apply(pf.params([socrates])))

    # Desenha o grafo.
    g = gd.GraphDrawer(proof)
    g.draw()