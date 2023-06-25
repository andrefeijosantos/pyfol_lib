class Table:
    def __init__(self, keys):
        self.total_data = 0
        self.data = dict()
        for key in keys:
            self.data[key] = []
        self.data_list = []

    def Add(self, key, item):
        self.data[key].append(item)
        self.total_data += 1
        self.data_list.append((key, len(self.data[key])-1))

    def Exists(self, key, item):
        for elem in self.data[key]:
            if elem == item:
                return True
        return False

    def Size(self, key):
        return len(self.data[key])

    def GetIf(self, key, compare):
        for elem in self.data[key]:
            if compare(elem):
                return elem
        return None

    def toList(self):
        elems_list = []
        for k in self.data.keys():
            for elem in self.data[k]:
                elems_list.append(elem)
        return elems_list

    def __len__(self):
        return self.total_data

    def __getitem__(self, idx):
        return self.data[self.data_list[idx][0]][self.data_list[idx][1]]