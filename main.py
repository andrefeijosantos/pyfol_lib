from command_reader import CommandReader

import pyfol.types.basics as pf
import pyfol.prover.prover as pr
import pyfol.env.environment as env

if __name__ == "__main__":
    env = env.ProofEnvironment() # Define um ambiente de prova.
    prover = pr.AutomatedProver(env)

    # Define uma nova constante ao ambiente.
    socrates = env.addConst(name="Socrates")

    # Define novos predicados.
    homem  = env.addPred(name="Homem", num_args=1)
    mortal = env.addPred(name="Mortal", num_args=1)

    # Supõe uma proposição.
    homem_socrates = homem.apply(pf.params([socrates]))
    env.sup(homem_socrates)

    # Supõe um predicado: Homem(x) => Mortal(x)
    env.sup(homem.apply(pf.params([env.x(1)])) >> mortal.apply(pf.params([env.x(1)])))

    # Provar.
    prover.prove(mortal.apply(pf.params([socrates])))