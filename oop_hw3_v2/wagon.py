from faker import Faker

from aqa_course.oop_hw3_v2.train import Train

fake = Faker()


class Wagon:

    def __init__(self):
        self.wagon_number = [Train().list_of_wagons]
        self.list_of_passengers = [fake.unique.first_name() for i in range(10)]

    def __str__(self):
        return f' {self.__class__.__name__}: {{\n\twagon: \'{self.wagon_number}\'\n\t passengers:\n' \
               f'{self.list_of_passengers}' \
               f'\n\t}}'

    def add_passenger(self, passenger: str):
        return self.list_of_passengers.append(passenger)

    def __len__(self):
        return len(self.list_of_passengers)


c = Wagon()




print(c)

