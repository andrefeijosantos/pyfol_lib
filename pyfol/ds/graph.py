class Graph:
    def __init__(self):
        self.graph = dict()
        self.start_list = []

    def start(self, _start_list):
        for elem in _start_list: self.start_list.append(elem)

    def addVertice(self, v):
        self.graph[v] = set()

    def addConection(self, v1, v2):
        try:
            self.graph[v1].add(v2)
        except:
            self.graph[v1] = set()
            self.graph[v1].add(v2)

    def print(self):
        for k in self.graph.keys():
            print(k, self.graph[k])

    def __getitem__(self, item):
        try:
            return self.graph[item]
        except: return []