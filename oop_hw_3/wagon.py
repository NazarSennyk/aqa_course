from aqa_course.oop_hw_3.train import Train


class Wagon(Train):
    def __init__(self):
        super().__init__()

    def add_passenger(self, passenger: str):
        return self.list_of_passengers.append(passenger)

    def __len__(self, arg):
        if arg == self:
            return len(self.list_of_wagons)
        elif arg == Wagon:
            return len(self.list_of_passengers)

c = Wagon()
