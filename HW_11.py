from abc import ABC, abstractmethod
import random


class SchoolPersonal(ABC):
    School_money = 0

    @abstractmethod
    def __str__(self):
        pass

    def __init__(self, name, surname, salary):
        """
        Init of a class
        :param name:
        :param surname:
        :param salary:
        """
        self.name = name
        self.surname = surname
        self.salary = salary
        SchoolPersonal.School_money += self.salary
        if type(self) == Teacher:
            Teacher.teacher_list.append(f'{self.name} {self.surname}')
        elif type(self) == TechPersonal:
            TechPersonal.list_person.append(f'{self.name} {self.surname}')


class Teacher(SchoolPersonal):
    teacher_list = []

    def __str__(self):
        return f'{self.salary}'


class TechPersonal(SchoolPersonal):
    list_person = []

    def __str__(self):
        return f'{self.salary}'

    def directors_assignment(self):
        """
        Assigmaent of new director of a school
        :return: new director from teacher_list
        """
        director = self.director
        self.director = random.choice(self.teachers_list)
        self.teachers_list = self.teachers_list.remove(self.director)


teacher1 = Teacher('Bob', 'Wolf', 2000)
teacher2 = Teacher('Tom', 'Walles', 3000)
teacher3 = Teacher('Alex', 'Good', 30300)
teacher4 = Teacher('Goof', 'Ben', 30000)
teacher5 = Teacher('Alek','Bold', 7000)


class School:

    def __init__(self, name, director, teachers_list, tec_personal_list, month_salary):
        """
        Init for school class
        :param name:
        :param director:
        :param teachers_list:
        :param tec_personal_list:
        :param month_salary:
        """
        self.name = name
        self.director = director
        self.teachers_list = teachers_list
        self.tec_personal_list = tec_personal_list
        self.__month_salary = month_salary

    @property
    def get_list_people(self):
        """
        returns a list o all employee
        :return: list
        """
        all_person = [self.director, self.teachers_list, self.tec_personal_list]
        return all_person

    def directors_assignment(self):
        """
        Assings a new director
        :return:
        """
        Teacher.teacher_list.append(self.director)
        self.director = random.choice(self.teachers_list)
        self.teachers_list = self.teachers_list.remove(self.director)

    @staticmethod
    def add_teacher(name, surname, salary):
        Teacher(name, surname, salary)


tec_person = TechPersonal('Alen', 'Wolks', 700)
tec_person2 = TechPersonal('Vova', 'Loft', 800)
tec_person3 = TechPersonal('Dima', 'Red', 900)


new_school = School('Adam_West', random.choice(Teacher.teacher_list), Teacher.teacher_list, TechPersonal.list_person, 1000000)
teacher_ls = Teacher.teacher_list
salary_amount = SchoolPersonal.School_money
new_teacher = School
new_teacher.add_teacher('Taras', 'Petrov', 19000)


