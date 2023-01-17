from oop_hw.predators import Predators


class Shark(Predators):
    def __init__(self, age: int, name: str, gender: str, hunt_in_pride: bool):
        super().__init__(age, name, gender, hunt_in_pride)

    @staticmethod
    def hunt_in_pride(victim: str):
        return print(f' Your pride attack {victim}')

    def feed_animal(self, food: str):
        return print(f' Your animal eat {food}')


Shark(3, 'Wolly', 'Male', True).hunt_in_pride('Whales')
