import heapq
import copy
import math
import time

import pyfol.env.environment
from pyfol.ds.graph import Graph
from pyfol.prover.q_learning_agent import QLearningAgent
from pyfol.prover.q_learning_agent import LogicalWorld
from pyfol.types.prop import Prop
from pyfol.types.temp_prop import TempProp

from pyfol.prover.proof_writer import ProofWriter

class Proof:
    def __init__(self, _env, _verbose=True):
        self.env = _env
        self.prop_to_prove_1 = None
        self.prop_to_prove_2 = None
        self.time = 60
        self.agent = None
        self.verbose = _verbose

    def dist(self, prop):
        self.agent.getNodeValue(prop.getHash())

    def prove(self, prop):
        self.header()

        if isinstance(prop, TempProp) or isinstance(prop, Prop):
            self.prop_to_prove_1 = ~prop
        else:
            self.prop_to_prove_1 = ~prop.prop.pred1
            self.prop_to_prove_2 = ~prop.prop.pred2
            self._prove_(self.prop_to_prove_2)
        self._prove_(self.prop_to_prove_1)

    def _prove_(self, prop):
        self.world = LogicalWorld(prop, self.env.absurdum, self.env.inf_rules)
        self.agent = QLearningAgent(self.world, _verbose=self.verbose)
        self.agent.run()

        return
        proof, aux_data = self.AStar(prop)
        if proof != None: 
            ProofWriter(self.env).print(proof)
            print("\n□ Q.E.D")
            print("Solved in %.4f seconds" % aux_data)
            print()
        else:
            print(aux_data, "\n")

    def AStar(self, prop):
        to_visit, visited = [(0, prop, [self.startString()])], set()
        found = dict(); heapq.heapify(to_visit)

        start_time = time.time()
        while len(to_visit) > 0:
            if (time.time() - start_time) >= self.time: 
                return (None, "Time limit reached")

            # Posição de menor valor.
            value, node, ops = heapq.heappop(to_visit)
            visited.add(node.getHash())
            found[node.getHash()] = True

            # Se chegar em um absurdo, para.
            if node.getHash() in self.env.absurdum: return (ops, time.time() - start_time)

            # Gera os vizinhos a partir das regras de inferência e busca o menor caminho.
            deductions = self.env.getRules().applyRule(node)
            for (deduction, string) in deductions: 
                if deduction in visited: continue
                if node.getHash() in found.keys() and deduction not in visited: 
                    heapq.heappush(to_visit, (value + 1 + self.dist(deduction), deduction, ops + [string]))

        return (None, "Couldn't prove")



    def startString(self):
        string = ""
        ### ADICIONAR PROPOSIÇÕES E PREDICADOS MOLECULARES AQUI ###
        return string + f"{self.prop_to_prove_1}".replace("<Pyfol.TempProp NOT ", '~').rstrip('>')

    def setTime(self, _time):
        self.time = _time

    def header(self):
        print("PyFOL Prover - version 1.0")
        print("Time Limit:", self.time, "seconds\n")
        print(f"Proof Environment with {len(self.env.consts)} constant(s);", end="")
        print(f" {len(self.env.preds)} atomic predicate(s); {len(self.env.props)} proposition(s) ", end="")
        print(f"and {len(self.env.compound_preds)} compound predicate(s) assumed\n")

    def getAgent(self):
        return self.agent
    
    def getTerminalStates(self):
        return self.agent.getTerminalStatesStrIds()