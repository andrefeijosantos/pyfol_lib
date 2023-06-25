class ProofWriter:
    def __init__(self, _env):
        self.env = _env
        self.ids = dict()
        self.ids['1'] = "Modus Ponens"
        self.ids['2'] = "Modus Tollens"

    def print(self, proof):
        # for prop in self.env.getProps():
        #     print(prop.toString(), "| Hyp")
        print(proof[0], "| Hyp")
        for i in range(1, len(proof)):
            line = proof[i].split(';')
            proof_line = self.ids[line[0]]
            proof_line += "(" + self.env.preds[int(line[1])].name + " => " + self.env.preds[int(line[2])].name + ", "
            proof_line += "~" + self.env.preds[int(line[2])].name + "("

            line = line[3][:len(line[3])-1].split(' ')
            for i in range(len(line)-1): proof_line += self.env.consts[int(line[i])].name + ","
            proof_line += self.env.consts[int(line[len(line)-1])].name

            proof_line += "))"
            print(proof_line)