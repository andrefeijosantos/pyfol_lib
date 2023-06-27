import pyfol.prover.prover as pr
import pyfol.env.environment as env

import pyfol.ds.graph_drawer as gd

if __name__ == "__main__":
    # Define um ambiente de prova.
    env = env.ProofEnvironment() 

    # === PRIMEIRA PROVA: Mortal(Socrates) := True ===
    # Define uma nova constante ao ambiente.
    socrates = env.addConst(name="Socrates")

    # Define novos predicados.
    homem  = env.addPred(name="Homem", num_args=1)
    animal  = env.addPred(name="Animal", num_args=1)
    mortal = env.addPred(name="Mortal", num_args=1)
    imortal = env.addPred(name="Imortal", num_args=1)
    irracional = env.addPred(name="Irracional", num_args=1)

    # Supõe uma proposição.
    env.sup(~irracional.apply([socrates]))

    # Supõe um predicado: Homem(x) => Mortal(x)
    env.sup(homem.apply([env.x(1)]) >> mortal.apply([env.x(1)]))
    env.sup(~mortal.apply([env.x(1)]) >> imortal.apply([env.x(1)]))
    env.sup(imortal.apply([env.x(1)]) >> ~mortal.apply([env.x(1)]))
    env.sup(~homem.apply([env.x(1)]) >> irracional.apply([env.x(1)]))
    env.sup(~homem.apply([env.x(1)]) >> animal.apply([env.x(1)]))

    # Provar.
    env.prove(pr.Proof(mortal.apply([socrates]), _verbose=False))

    # Desenha o grafo.
    g = gd.GraphDrawer(env)
    g.draw()

    # === FIM DA PRIMEIRA PROVA ===

    # === SEGUNDA PROVA: Divindade(Socrates) := False ===
    # Mais predicados a serem adicionados no contexto.
    deus_grego = env.addPred(name="DeusGrego", num_args=1)
    divindade = env.addPred(name="Divindade", num_args=1)
    cultuado = env.addPred(name="Cultutado", num_args=1)
    sobrenatural = env.addPred(name="Sobrenatural", num_args=1)

    # Novas deduções.
    env.sup(deus_grego.apply([env.x(1)]) >> imortal.apply([env.x(1)]))
    env.sup(divindade.apply([env.x(1)]) >> deus_grego.apply([env.x(1)]))
    env.sup(divindade.apply([env.x(1)]) >> cultuado.apply([env.x(1)]))
    env.sup(divindade.apply([env.x(1)]) >> sobrenatural.apply([env.x(1)]))

    # Provar.
    env.prove(pr.Proof(~divindade.apply([socrates]), _verbose=False))

    # Desenha o grafo.
    g = gd.GraphDrawer(env)
    g.draw()

    # === FIM DA SEGUNDA PROVA ===