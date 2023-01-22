from random import randint
from faker import Faker

fake = Faker()


class Train:
    def __init__(self):
        self.__locomotive = 1
        self.list_of_wagons = [1]
        self.list_of_passengers = [fake.unique.first_name() for i in range(10)]

    def __str__(self):
        return f' {self.__class__.__name__}: {{\n\twagon: {self.list_of_wagons}\n\t passengers:{self.list_of_passengers}\t}}'

    def add_wagon(self):
        self.list_of_wagons += [randint(1, 20)]

c = Train()
print(c)