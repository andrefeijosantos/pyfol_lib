class ProofWriter:
    def print(self, proved_prop, agent):
        print("====================================")
        print("               PROOF                  \n")

        max_length, lines, state = 0, [], proved_prop
        while state.getStrId() not in agent.world.end:
            state = agent.getPolicy(state)
            if state == None: break
            state_str = state.toString()
            lines += [state_str]
            if len(state_str) > max_length:
                max_length = len(state_str)

        print(agent.world.start.toString(), " "*(max_length-len(agent.world.start.toString())) + "| Hyphotesis")
        state = agent.world.start
        while True:
            if state.getStrId() not in agent.world.end: break

            state = agent.getPolicy(state)
            if state == None: break
            print(state.toString(), " "*(max_length-len(state.toString())) + "| ")

        print(state.toString(), " "*(max_length-len(state.toString())) + "| Fallacy")
        print("\nQ.E.D. □")
        print("====================================\n\n")