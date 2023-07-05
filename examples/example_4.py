import pyfol.prover.prover as pr
import pyfol.env.environment as environment

import pyfol.ds.graph_drawer as gd

if __name__ == "__main__":
    # Define um ambiente de prova.
    env = environment.ProofEnvironment() 

    q_1, q_2, q_3 = env.addPred(name="q1",num_args=1), env.addPred(name="q2",num_args=1), env.addPred(name="q3",num_args=1)
    q_4, q_5 = env.addPred(name="q4",num_args=1), env.addPred(name="q5",num_args=1)

    p_1, p_2, p_3 = env.addPred(name="p1",num_args=1), env.addPred(name="p2",num_args=1), env.addPred(name="p3",num_args=1)
    p_4, p_5, p_6 = env.addPred(name="p4",num_args=1), env.addPred(name="p5",num_args=1), env.addPred(name="p6",num_args=1)

    s_1, s_2, s_3 = env.addPred(name="s1",num_args=1), env.addPred(name="s2",num_args=1), env.addPred(name="s3",num_args=1)
    s_4, s_5, s_6 = env.addPred(name="s4",num_args=1), env.addPred(name="s5",num_args=1), env.addPred(name="s6",num_args=1)

    t_1, t_2, t_3 = env.addPred(name="t1",num_args=1), env.addPred(name="t2",num_args=1), env.addPred(name="t3",num_args=1)
    t_4, t_5, t_6 = env.addPred(name="t4",num_args=1), env.addPred(name="t5",num_args=1), env.addPred(name="t6",num_args=1)

    env.sup(~t_1.apply([env.x(1)]) | t_2.apply([env.x(1)]))
    env.sup(~t_1.apply([env.x(1)]) | t_4.apply([env.x(1)]))
    env.sup(t_2.apply([env.x(1)]) >> t_4.apply([env.x(1)]))
    env.sup(t_4.apply([env.x(1)]) >> t_2.apply([env.x(1)]))
    env.sup(t_4.apply([env.x(1)]) >> t_5.apply([env.x(1)]))
    env.sup(t_5.apply([env.x(1)]) >> t_4.apply([env.x(1)]))
    env.sup(t_4.apply([env.x(1)]) >> t_3.apply([env.x(1)]))
    env.sup(t_3.apply([env.x(1)]) >> q_1.apply([env.x(1)]))

    env.sup(q_1.apply([env.x(1)]) >> q_2.apply([env.x(1)]))
    env.sup(q_1.apply([env.x(1)]) >> q_4.apply([env.x(1)]))
    env.sup(q_2.apply([env.x(1)]) >> q_4.apply([env.x(1)]))
    env.sup(q_4.apply([env.x(1)]) >> q_2.apply([env.x(1)]))
    env.sup(q_4.apply([env.x(1)]) >> q_5.apply([env.x(1)]))
    env.sup(q_5.apply([env.x(1)]) >> q_4.apply([env.x(1)]))
    env.sup(q_4.apply([env.x(1)]) >> q_3.apply([env.x(1)]))
    env.sup(q_3.apply([env.x(1)]) >> q_4.apply([env.x(1)]))

    env.sup(q_1.apply([env.x(1)]) >> q_2.apply([env.x(1)]))
    env.sup(q_1.apply([env.x(1)]) >> q_4.apply([env.x(1)]))
    env.sup(q_2.apply([env.x(1)]) >> q_4.apply([env.x(1)]))
    env.sup(q_4.apply([env.x(1)]) >> q_2.apply([env.x(1)]))
    env.sup(q_4.apply([env.x(1)]) >> q_5.apply([env.x(1)]))
    env.sup(q_5.apply([env.x(1)]) >> q_4.apply([env.x(1)]))
    env.sup(q_4.apply([env.x(1)]) >> q_3.apply([env.x(1)]))
    env.sup(q_3.apply([env.x(1)]) >> q_4.apply([env.x(1)]))

    env.sup(q_1.apply([env.x(1)]) >> p_5.apply([env.x(1)]))
    env.sup(p_1.apply([env.x(1)]) >> p_2.apply([env.x(1)]))
    env.sup(p_1.apply([env.x(1)]) >> p_4.apply([env.x(1)]))
    env.sup(p_2.apply([env.x(1)]) >> p_4.apply([env.x(1)]))
    env.sup(p_4.apply([env.x(1)]) >> p_2.apply([env.x(1)]))
    env.sup(p_4.apply([env.x(1)]) >> p_5.apply([env.x(1)]))
    env.sup(q_2.apply([env.x(1)]) >> p_2.apply([env.x(1)]))
    env.sup(q_4.apply([env.x(1)]) >> p_5.apply([env.x(1)]))
    env.sup(p_5.apply([env.x(1)]) >> p_4.apply([env.x(1)]))

    env.sup(q_1.apply([env.x(1)]) >> s_3.apply([env.x(1)]))
    env.sup(s_1.apply([env.x(1)]) >> s_2.apply([env.x(1)]))
    env.sup(s_1.apply([env.x(1)]) >> s_4.apply([env.x(1)]))
    env.sup(s_2.apply([env.x(1)]) >> s_4.apply([env.x(1)]))
    env.sup(p_4.apply([env.x(1)]) >> s_2.apply([env.x(1)]))
    env.sup(p_4.apply([env.x(1)]) >> s_5.apply([env.x(1)]))
    env.sup(p_2.apply([env.x(1)]) >> s_1.apply([env.x(1)]))
    env.sup(p_2.apply([env.x(1)]) >> s_3.apply([env.x(1)]))
    env.sup(p_2.apply([env.x(1)]) >> s_2.apply([env.x(1)]))
    env.sup(p_2.apply([env.x(1)]) >> s_4.apply([env.x(1)]))
    env.sup(p_2.apply([env.x(1)]) >> s_5.apply([env.x(1)]))
    env.sup(p_2.apply([env.x(1)]) >> s_6.apply([env.x(1)]))
    env.sup(q_4.apply([env.x(1)]) >> s_5.apply([env.x(1)]))
    env.sup(s_5.apply([env.x(1)]) >> s_4.apply([env.x(1)]))

    env.sup(~q_3.apply([]))

    env.prove(pr.Proof(~t_1.apply([]), _verbose=False))

    # Desenha o grafo.
    g = gd.GraphDrawer(env)
    g.draw()