class ProofWriter:
    def print(self, proved_prop, agent, inf_rules):
        print("====================================")
        print("               PROOF                  \n")

        max_length, lines, state = 0, [], proved_prop
        while not agent.isTerminalState(state):
            state = agent.getPolicy(state)
            if state == None: break
            state_str = state.toString()
            lines += [state_str]
            if len(state_str) > max_length:
                max_length = len(state_str)

        print(agent.world.start.toString(), " "*(max_length-len(agent.world.start.toString())) + "| Hyphotesis")
        state = agent.world.start
        parent = agent.world.start
        while True:
            parent = state
            state = agent.getPolicy(state)
            if state == None or agent.isTerminalState(state): break
            print(state.toString(), " "*(max_length-len(state.toString())) + "|", 
                  inf_rules[parent.prop.pred.getId()+1, state.prop.pred.getId()+1].setProp(parent))

        print(state.toString(), " "*(max_length-len(state.toString())) + "| Fallacy")
        print("\nQ.E.D. □")
        print("====================================\n\n")