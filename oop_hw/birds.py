from abc import ABC, abstractmethod
from oop_hw.animals import Animal


class Bird(Animal):
    def __init__(self, age: int, name: str, gender: str, hunt_in_pride: bool):
        super().__init__(age, name, gender)
        self.hunt_in_pride = hunt_in_pride

    @staticmethod
    def create_a_nest(materials: str):
        return print(f' your bird created a nest from {materials}')

    @staticmethod
    def bath_you_bird():
        super().bath_animal('Parrot')
        super().feed_animal('Warms')
        return print(f' Your bird is bathing')

    def feed_animal(self, food: str):
        return print(f' Your animal eat {food}')


parrot = Bird(1, 'Jago', 'Male', False).bath_animal('Jago')


