

class Train:

    def __init__(self):
        self.__locomotive = 1
        self.list_of_wagons = []

    def __len__(self):
        print(self.list_of_wagons)
        return 0

    def add_wagon(self, wagon):
        return self.list_of_wagons.append(wagon)



trn = Train()


print(len(trn))
