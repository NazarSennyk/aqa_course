from abc import ABC, abstractmethod
from random import randint, choice
from typing import Union
import faker
from faker import Faker

fake = Faker()


class SchoolPersonal(ABC):
    def __init__(self, name: str, salary: Union[int, float]):
        self.name = name
        self.salary = salary

    @abstractmethod
    def __str__(self):
        pass


class Teacher(SchoolPersonal):
    def __str__(self):
        return f' Hello my name is {self.name} with salary {self.salary} I\'m your new principal'


class TechnicalPersonal(SchoolPersonal):
    def __str__(self):
        return f' Hello my name is {self.name} with salary {self.salary} I\'m your new technical staff'


class School:
    def __init__(self, name: str, director: Teacher, teachers_list: int = 15, tech_personal_list: int = 8):
        self.name = name
        self.director = director
        self.teachers_list = [Teacher(fake.name(), randint(5000, 10000)) for position in range(teachers_list)]
        self.tech_personal_list = [TechnicalPersonal(fake.name(), randint(3000, 7000)) for position in range(tech_personal_list)]

    @property
    def get_total_salary(self):
        all_employee = []
        all_employee.append(self.director)
        all_employee += self.teachers_list
        all_employee += self.tech_personal_list
        total_money_employee = sum((obj.salary for obj in all_employee))
        return total_money_employee

    def director_assignment(self):
        old_director = self.director
        new_director = self.teachers_list.pop()
        self.director = new_director
        self.teachers_list.append(old_director)

    @staticmethod
    def add_teacher(name: str, salary: Union[int, float]):
        Teacher(name, salary)


school2 = School('Adam_west_school', Teacher('Ben Wilson', 8000))
print(school2.teachers_list)
print(school2.get_total_salary)
school2.add_teacher('Will Smith', 4500)
school2.director_assignment()

