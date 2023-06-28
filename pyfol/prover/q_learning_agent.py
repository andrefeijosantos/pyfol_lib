import random, time
from pyfol.ds.graph import Graph 
from pyfol.prover.proof_writer import ProofWriter 

from pyfol.prover.proof_data import ProofData

class Episode:
    def __init__(self, _ep):
        self.ep = _ep

    def setResults(self, _rntm, _reward, _final_state):
        self.rntm = _rntm
        self.reward = _reward
        self.final_state = _final_state

    def header(self):
        print("===================")
        print(f"RUNNING EPISODE {self.ep}:\n")

    def results(self):
        print(f"Runtime: {self.rntm:.2f}")
        print(f"Got Reward: {self.reward} (found: {self.final_state.toString()})")
        print("===================\n")

class LogicalWorld:
    def __init__(self, _start, _end, _inf_rules):
        self.start = _start
        self.end = _end

        self.inf_rules = _inf_rules
        self.graph     = Graph()

class QLearningAgent:
    def __init__(self, _logical_world, _alpha=0.9, _epsilon=0.5, _discount=0.9, _num_episodes=10, _verbose=True):
        self.alpha = _alpha
        self.epsilon = _epsilon
        self.DISCOUNT = _discount
        self.NUM_EPISODES = _num_episodes
        self.verbose = _verbose

        self.q_values = dict()
        self.world = _logical_world
        self.id_to_name = dict()

    # Seta cada parâmetro individualmente.
    def set(self, _alpha, _epsilon, _discount, _num_episodes, _verbose):
        if _alpha != -1: self.alpha = _alpha
        if _epsilon != -1: self.epsilon = _epsilon
        if _discount != -1: self.DISCOUNT = _discount
        if _num_episodes != -1: self.NUM_EPISODES = _num_episodes
        if _verbose != -1: self.verbose = _verbose

    def setWorld(self, _logical_world):
        self.world = _logical_world

    def setVerbose(self, _verbose):
        self.verbose = _verbose

    # === FUNÇÕES DE APRENDIZADO Q ===
    # Retorna o valor Q de um estado indo para outro.
    def getQValue(self, state, next_state):
        if (state.getStrId(),next_state.getStrId()) not in self.q_values.keys():
            self.q_values[(state.getStrId(),next_state.getStrId())] = 0
        return self.q_values[(state.getStrId(),next_state.getStrId())]

    # Escolhe uma ação para tomar.
    def getAction(self, state):
        possible_actions = self.world.inf_rules.getDeductions(state)
        next_state = None

        if len(possible_actions) > 0 and random.uniform(0.0, 1.0) < self.epsilon: 
            next_state = random.choice(possible_actions)
        else: next_state = self.getPolicy(state)

        return next_state

    # Atualiza o valor de um par de (state, next_state)
    def update(self, state, next_state, reward):
      self.q_values[(state.getStrId(),next_state.getStrId())] = (1-self.alpha)*self.getQValue(state,next_state)
      self.q_values[(state.getStrId(),next_state.getStrId())] += self.alpha*(reward + self.DISCOUNT*self.getValue(next_state))

    # Retorna a melhor ação a se tomar diante ed um estado.
    def getPolicy(self, state):
        possible_actions = self.world.inf_rules.getDeductions(state)
        if len(possible_actions) == 0: return None

        best, best_value = 0, self.getQValue(state, possible_actions[0])
        for i in range(1,len(possible_actions)):
            if self.getQValue(state, possible_actions[i]) > best_value:
                best = i
                best_value = self.getQValue(state, possible_actions[i])
            elif self.getQValue(state, possible_actions[i]) == best_value:
                best = random.choice([best, i])

        return possible_actions[best]

    # Retorna o melhor valor Q de um estado.
    def getValue(self, state):
        possible_actions = self.world.inf_rules.getDeductions(state)
        if len(possible_actions) == 0: return 0
        return max([self.getQValue(state, action) for action in possible_actions])

    # Retorna o valor de um nó.
    def getNodeValue(self, state):
        return self.getValue(state)

    # === FIM DAS FUNÇÕES DE APRENDIZADO Q ===



    # === FUNÇÕES DE EXECUÇÃO ===
    # Roda todos os episódios do aprendizado Q para o agente.
    def run(self): 
        proved = 0
        start = time.time()
        for ep in range(self.NUM_EPISODES): 
            if self.run_episode(ep+1): proved += 1
        Tf = time.time() - start

        print(f"Number of episodes: {self.NUM_EPISODES}")
        print(f"Runtime: {Tf:.2f}")

        if proved > 0:
            print(f"\nProposition {(~self.world.start).toString()} proved.")
            self.world.end.add((~self.world.start).getStrId())
            ProofWriter().print(self.world.start, self)
        else:
            print(f"Couldn't prove {(~self.world.start).toString()}.")
            

        return ProofData(proved > 0, self.world.start, Tf, self.NUM_EPISODES, proved, len(self.world.graph.vertex()))

    # Roda apenas um episódio do aprendizado.
    def run_episode(self, ep):
        if self.verbose == True: ep = Episode(ep); ep.header()
        reward, parents, state, found = -5, [], self.world.start, set()
        self.id_to_name[state.getStrId()] = state.toString()
        rewards = [0]
        # self.world.end.add((~self.world.start).getStrId())  <============= CONSIDERAR DEPOIS

        # Caminha pelo grafo até chegar em algo que prove a proposição ou
        # que não tenha mais para onde ir.
        start_time = time.time()
        while state.getStrId() not in self.world.end:
            if state.getStrId() in found: rewards.append(-5); break # MUDAR PARA NUMERICO DEPOIS
            found.add(state.getStrId())                             # MUDAR PARA NUMERICO DEPOIS

            parents.append(state)
            next_state = self.getAction(state)

            if next_state == None: rewards.append(-5); break
            elif next_state.getStrId() == self.world.start.getStrId(): 
                self.world.graph.addConection(state.getStrId(), next_state.getStrId())
                rewards.append(-5); break
            else: 
                self.world.graph.addConection(state.getStrId(), next_state.getStrId())
                state = next_state
                rewards.append(-0.5)
            self.id_to_name[state.getStrId()] = state.toString()
        final_state = state
        if rewards[len(rewards)-1] == -0.5:
            self.proved, reward = True, 5
            rewards[len(rewards)-1] = 5

        # Atualiza os valores Q de cada par (estado, proximo_estado)
        while len(parents) > 0:
            parent = parents.pop(len(parents)-1)
            self.update(parent, state, rewards.pop(len(rewards)-1))
            state = parent
        if reward == 5: self.proved = True
        if self.verbose == True: ep.setResults(time.time() - start_time, reward, final_state); ep.results()
        return reward == 5

    def getGraph(self):
        return self.world.graph
    
    def getTerminalStatesStrIds(self):
        TERMINAL_STATES = set()
        for state in self.world.end:
            TERMINAL_STATES.add(state)
        return TERMINAL_STATES

    # === FIM DAS FUNÇÕES DE EXECUÇÃO ===