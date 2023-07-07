from pyfol.ds.table import Table
from pyfol.ds.graph import Graph

from pyfol.logical_operators.logical_or import *
from pyfol.logical_operators.logical_and import *

from pyfol.types.const import Const
from pyfol.types.user_const import UserConst
from pyfol.types.pred import Pred
from pyfol.types.prop import Prop
from pyfol.types.temp_prop import TempProp
from pyfol.types.temp_pred import TempPred
from pyfol.types.var import Var
from pyfol.prover.q_learning_agent import QLearningAgent
from pyfol.prover.q_learning_agent import LogicalWorld

from pyfol.ds.rules import Rules

class ProofEnvironment:
    def __init__(self):
        # Suposições do usuário.
        keys = [chr(c) for c in range(65, 91)]
        keys += ["OR"]
        self.consts = Table(keys)
        self.preds  = Table(keys)
        self.props  = Table(keys) 
        self.compound_preds  = Table(keys)

        # Estruturas de dados.
        self.graph     = Graph()
        self.pred_ids  = dict()
        self.inf_rules = Rules(self.pred_ids)
        self.absurdum  = set()
        self.defined_names  = Table(keys)
        self.absurdum_preds = set()

        # Agente que "caminha" pelo ambiente de prova.
        self.time = 60
        self.agent = QLearningAgent(None)

    # ===== DEFINIÇÃO DO AMBIENTE DE PROVA =====
    # Os métodos abaixo servem para popular o ambiente de provas.

    # === DEFINIÇÕES DE ENTIDADES ===
    # Define uma nova constante para o ambiente.
    def addConst(self, name=""):
        if name == "": name = "a_" + len(self.consts)

        const = UserConst(name, len(self.consts))
        self.consts.Add(name[0].upper(), const)
        self.defined_names.Add(name[0].upper(),name)
        return const

    # Define um novo predicado para o ambiente.
    def addPred(self, name="", num_args=1):
        if name == "": name = "P_" + len(self.consts)

        pred = Pred(name, num_args, len(self.preds))
        self.preds.Add(name[0].upper(),pred)
        self.defined_names.Add(name[0].upper(),name)
        self.pred_ids[len(self.preds)] = pred
        return pred

    # === FIM DAS DEFINIÇÕES DE ENTIDADES ===

    # === FUNÇÕES DE HIPÓTESES LÓGICAS ===
    def sup(self, entity):
        if isinstance(entity, Prop):
            self.graph.addVertice(TempProp(entity,True))
            self.absurdum.add((~entity).getStrId())
            self.props.Add(entity.pred.name[0].upper(), entity)
        elif isinstance(entity,TempProp):
            self.graph.addVertice(TempProp(entity,entity.hyp).getHash())
            self.absurdum.add((~entity).getStrId())
            self.props.Add(entity.prop.pred.name[0].upper(), entity.prop)
        elif isinstance(entity, LogicalOR):
            entity.apply(self.inf_rules)
            self.compound_preds.Add("OR", entity)
        elif isinstance(entity, TempPred):
            self.absurdum_preds.add(entity.pred.name)
        elif isinstance(entity, LogicalAND):
            self.sup(entity.temp_pred1)
            self.sup(entity.temp_pred2)

    # === FIM DAS FUNÇÕES DE HIPÓTESES LÓGICAS ===


    # === MÉTODOS GET ===
    #Retorna um predicado.
    def getPred(self, name):
        return self.preds.GetIf(name[0].upper(), lambda a : a.name == name)

    #Retorna uma proposição.
    def getProp(self, name):
        return self.props.GetIf(name[0].upper(), lambda a : a.name == name)

    #Retorna uma constante.
    def getConst(self, name):
        return self.consts.GetIf(name[0].upper(), lambda a : a.name == name)

    # Retorna todas as constantes do ambiente.
    def getConsts(self):
        return self.consts.toList()

    # Retorna todos os predicados do ambiente.
    def getPreds(self):
        return self.preds.toList()

    # Retorna todas as proposições do ambiente.
    def getProps(self):
        return self.props.toList()

    # Retorna as regras.
    def getRules(self):
        return self.inf_rules

    # Retorna uma variáveis.
    def x(self, num): return Var("x" + str(num))
    def y(self, num): return Var("y" + str(num))
    def z(self, num): return Var("z" + str(num))

    # Retorna uma constante não criada pelo usuário.
    def a(self, num): return Const("a" + str(num))
    def b(self, num): return Const("b" + str(num))
    def c(self, num): return Const("c" + str(num))

    # Retorna o grafo.
    def getGraph(self):
        return self.graph

    # === MÉTODOS SET ===
    def setTimeLimit(self, _time):
        self.time = _time

    def configureAgent(self, _alpha=-1, _epsilon=-1, _discount=-1, _num_episodes=-1, _verbose=-1):
        self.agent.set(_alpha, _epsilon, _discount, _num_episodes, _verbose)

    # === FIM DOS MÉTODOS GET ===
    # ===== FIM DA DEFINIÇÃO DO AMBIENTE DE PROVA =====


    # ===== MÉTODOS DE PROVA =====
    # Método público de prova: pode receber uma proposição molecular
    def prove(self, proof):
        self.header()
        return self._prove_(proof.prop_to_prove_1, proof.verbose)

    # Método privado de prova: prova cada proposição individualmente.
    def _prove_(self, prop, verbose):
        self.world = LogicalWorld(prop, self.absurdum.copy().union(self.absurdum_preds.copy()), self.inf_rules)
        self.agent.setWorld(self.world)
        self.agent.setVerbose(verbose)
        proof_data = self.agent.run()

        # Se foi provado, é uma verdade no contexto. Logo, é um absurdo negá-lo.
        if proof_data[0] != None: self.absurdum.add(proof_data[1].getStrId())

        return proof_data

    def header(self):
        print("PyFOL Prover - version 1.0")
        print("Time Limit:", self.time, "seconds\n")
        print(f"Proof Environment with {len(self.consts)} constant(s);", end="")
        print(f" {len(self.preds)} atomic predicate(s); {len(self.props)} proposition(s) ", end="")
        print(f"and {len(self.compound_preds)} compound predicate(s) assumed")

    # ===== FIM DOS MÉTODOS DE PROVA =====



# === FUNÇÕES AUXILIARES ===
# Verifica se um nome pode ser utilizado para uma entidade ou não.
def IsValidName(name):
    if ord(name[0]) < 65 or (ord(name[0]) > 90 and ord(name[0]) < 97) or ord(name[0]) > 122:
        return False

    for i in range(1, len(name)):
        if ord(name[i]) == 96 or ord(name[i]) < 48 or (ord(name[i]) > 59 and ord(name[i]) < 65):
            return False
        if (ord(name[i]) > 90 and ord(name[i]) < 95) or ord(name[i]) > 122:
                return False
    
    return True

# === FIM DAS FUNÇÕES AUXILIARES ===