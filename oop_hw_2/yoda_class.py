from oop_hw_2.jedi_class_main import Jedi

# Inheritance
class Yoda(Jedi):
    def __init__(self, lightsaber: bool, special_power: str, mana: int):
        super().__init__(lightsaber, special_power, mana)
        self.mana = 80

    # encapsulation
    def attack(self, other):
        if type(other) == Jedi:
            self.mana -= 15
            other.health -= 20
        else:
            self.mana -= 15
            other.health = 0

    def health_mana_increase(self, other):
        if type(other) == Jedi:
            self.mana += 20
            self.health += 20
        else:
            self.mana += 15
            self.health += 10

    # polymorphism
    @staticmethod
    def win_massage():
        print('I win, let the force be with you')


