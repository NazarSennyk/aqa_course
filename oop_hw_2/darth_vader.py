from oop_hw_2.jedi_class_main import Jedi

# Inheritance
class DarthVader(Jedi):
    def __init__(self, lightsaber: bool, special_power: str, mana: int):
        super().__init__(lightsaber, special_power, mana)
        self.space_ship_attack = True
        self.mana = 80

    # encapsulation
    def attack(self, other):
        if type(other) == Jedi:
            self.mana -= 20
            other.health -= 25
        else:
            self.mana -= 29
            other.health = 0

    def ship_attack(self, other):
        if type(other) == Jedi:
            self.space_ship_attack = False
            other.health -= 40
        else:
            self.space_ship_attack = False
            other.health = 0

    # polymorphism
    @staticmethod
    def win_massage():
        print('I win, feel the evil')