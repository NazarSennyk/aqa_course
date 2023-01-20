from abc import ABC, abstractmethod

#abstraction
# hiding
class Jedi(ABC):
    __health = 100
    __available_skill_points = 0
    # encapsulation
    # hiding
    def __init__(self, lightsaber: bool, special_power: str, mana: int):
        self.__lightsaber = lightsaber
        self.__special_power = special_power
        self.__mana = mana

    # abstraction
    @abstractmethod
    def attack(self, other):
        pass

    # encapsulation
    @property
    def show_health(self):
        return self.__health
