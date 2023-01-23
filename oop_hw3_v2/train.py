

class Train:

    def __init__(self):
        self.__locomotive = 1
        self.list_of_wagons = []

    def __len__(self):
        return len(self.list_of_wagons)

    def add_wagon(self, wagon: int):
        return self.list_of_wagons.append(wagon)



trn = Train()

trn.add_wagon(1)
trn.add_wagon(2)
trn.add_wagon(3)

print(len(trn.list_of_wagons))
