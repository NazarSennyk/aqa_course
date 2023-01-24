

class Train:

    def __init__(self):
        self.__locomotive = 1
        self.list_of_wagons = []

    def __len__(self):
        return self.list_of_wagons

    def add_wagon(self, wagon):
        return self.list_of_wagons.append(wagon)



trn = Train()


print(len(trn.list_of_wagons))
