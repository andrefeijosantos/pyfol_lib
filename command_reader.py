import pyfol
from pyfol.types.prop import Prop
from pyfol.types.forall_pred import ForAllPred

class CommandReader:
    def __init__(self, env):
        self.env = env
        self.execute = True

    # Recebe os comandos do usuário e os interpreta.
    def Execute(self):
        line = 1
        while self.execute:
            command = input(">> ")
            self.Interpret(command.rstrip().lstrip())
            line += 1

    # Interpreta um comando do usuário, para popular o ambiente de prova.
    def Interpret(self, command):
        if command == "" or command[0] == "#": return 
        if command == "end": 
            self.execute = False
            return

        # Separa comando útil de comentário.
        coment = command.find('#')
        if coment != -1: command = command[:coment]
        command = " ".join(command.split())

        # Define uma nova entidade no ambiente.
        if command.startswith("define"):
            command = command.lstrip("define ").split(' := ')

            if len(command) == 2:
                name, cnstrctr = command[0], command[1]
                if cnstrctr.startswith("Pred"):
                    args = int(cnstrctr[4:])
                    self.env.addPred(name=name, num_args=args)

            elif len(command) == 1:
                command = command[0]
                if command.endswith(" : const"):
                    consts = command.lstrip("define ")
                    consts = consts[:len(consts)-8].split(' ')
                    for c in consts: self.env.addConst(name=c)

        # Supõe um valor-verdade para um predicado ou proposição.
        elif command.startswith("sup"):
            self.env.sup(self.text2pred(command[4:]))

        elif command.startswith("|-"):
            print("provar")


    # === FUNÇÕES AUXILIARES ===
    # Converte uma string em um predicado composto ou proposição composta.
    def text2pred(self, line):
        if "\\/" in line:
            neg1, neg2 = False, False
            elem1, elem2 = line.split(" \\/ ")

            if elem1[0] == '~': neg1, elem1 = True, elem1[1:]
            if elem2[0] == '~': neg2, elem2 = True, elem2[1:]
            elem1, elem2 = self.getType(elem1), self.getType(elem2)

            if neg1: elem1 = ~elem1
            if neg2: elem2 = ~elem2

            return elem1 | elem2

        elif "/\\" in line:
            neg1, neg2 = False, False
            elem1, elem2 = line.split(" /\\ ")

            if elem1[0] == '~': neg1, elem1 = True, elem1[1:]
            if elem2[0] == '~': neg2, elem2 = True, elem2[1:]
            elem1, elem2 = self.getType(elem1), self.getType(elem2)

            if neg1: elem1 = ~elem1
            if neg2: elem2 = ~elem2

            return elem1 & elem2

        else:
            neg, elem = False, line
            if elem[0] == '~': neg1, elem = True, elem[1:]
            elem = self.getType(elem)
            if neg: elem = ~elem

            return elem

    # Verifica se é proposição. Se sim, retorna a proposição e as constantes
    # que usa. Senão, apenas retorna o predicado.
    def getType(self, line):
        ucs, cs, vs = False, False, False
        pred, args = line.split('('); 
        pred, args = self.env.getPred(pred), args[:len(args)-1]

        args = args.replace(" ","").split(',')
        u_consts, consts, vars, all_args = [], [], [], []
        for arg in args:
            if arg[0] == 'x' or arg[0] == 'y' or arg[0] == 'z':
                arg = self.env.x(arg[1:])
                vars.append(arg); vs = True
            elif arg[0] == 'a' or arg[0] == 'b' or arg[0] == 'c':
                arg = self.env.a(arg[1:])
                consts.append(arg); cs = True
            else:
                arg = self.env.getConst(arg)
                u_consts.append(arg); ucs = True
            all_args.append(arg)

        if vs and cs: return ForallExistsPred(pred, all_args)
        elif vs:      return ForAllPred(pred, all_args)
        elif cs:      return ExistsPred(pred, all_args)
        else:         return Prop(pred, u_consts)

    # === FIM DAS FUNÇÕES AUXILIARES ===