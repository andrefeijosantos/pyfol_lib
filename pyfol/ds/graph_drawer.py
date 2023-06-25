import networkx as nx
import matplotlib.pyplot as plt

class GraphDrawer:
    def __init__(self, _env):
        self.graph = _env.agent.world.graph
        self.root = _env.agent.world.start.getStrId()
        self.values = _env.agent.q_values
        self.convertion = _env.agent.id_to_name

        self.TERMINAL_STATES = _env.agent.getTerminalStatesStrIds()

    def draw(self):
        G = nx.DiGraph()
        pos, colors, outline = dict(), [(1,1,1)], [(34/255, 35/255, 36/255)]
        queue, visited = [(self.root, None)], dict()
        pos[self.root] = (50,50)

        while len(queue) > 0:
            node = queue.pop(0)
            if node[0] in visited.keys(): 
                G.add_edge(self.convertion[node[1]], self.convertion[node[0]])
                continue

            # Adiciona um vértice
            G.add_node(self.convertion[node[0]])

            # Conecta o vértice ao seu pai.
            if node[1] != None: 
                if node[0] in self.TERMINAL_STATES:
                    colors += [(2/255, 1, 0)]
                    outline += [(2/255, 115/255, 0)]
                elif self.values[node[1],(node[0])] > 0:
                    colors += [((1 + 0.1*self.values[node[1],(node[0])])/255, (80 + min(170, 30*self.values[node[1],(node[0])]))/255, 0)]
                    outline += [((1 + 0.1*self.values[node[1],(node[0])])/255, (80 + min(170, 30*self.values[node[1],(node[0])]))/255, 0)]
                elif self.values[node[1],(node[0])] == 0:
                    colors += [(212/255, 213/255, 214/255)]
                    outline += [(212/255, 213/255, 214/255)]
                else:
                    colors += [((238 + min(16, 30*self.values[node[1],(node[0])]))/255, 1/255, 1/255)]
                    outline += [((238 + min(16, 30*self.values[node[1],(node[0])]))/255, 1/255, 1/255)]
                G.add_edge(self.convertion[node[1]], self.convertion[node[0]])

            visited[node[0]] = True
            next_states = self.graph[node[0]]
            for state in next_states: 
                queue.append((state, node[0]))

        nx.draw(G,node_size=3000,with_labels=True,node_color=colors,edgecolors=outline)
        plt.margins(0.2)
        plt.show()