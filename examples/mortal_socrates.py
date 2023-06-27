import pyfol.prover.prover as pr
import pyfol.env.environment as env

import pyfol.ds.graph_drawer as gd

if __name__ == "__main__":
    # Define um ambiente de prova.
    env = env.ProofEnvironment() 

    # Define uma nova constante ao ambiente.
    socrates = env.addConst(name="Socrates")

    # Define novos predicados.
    homem  = env.addPred(name="Homem", num_args=1)
    mortal = env.addPred(name="Mortal", num_args=1)

    # Supõe uma proposição.
    homem_socrates = homem.apply([socrates])
    env.sup(homem_socrates)

    # Supõe um predicado: Homem(x) => Mortal(x)
    env.sup(homem.apply([env.x(1)]) >> mortal.apply([env.x(1)]))

    # Provar.
    env.prove(pr.Proof(mortal.apply([socrates]), _verbose=True))

    # Desenha o grafo.
    g = gd.GraphDrawer(env)
    g.draw()