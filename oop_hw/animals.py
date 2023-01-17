from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, age: int, name: str, gender: str):
        self.age = age
        self.name = name
        self.gender = gender

    @abstractmethod
    def feed_animal(self, food: str):
        return print(f' Your animal eat {food}')

    @staticmethod
    def bath_animal(animal: str):
        return print(f' Your {animal} takes a bath')
