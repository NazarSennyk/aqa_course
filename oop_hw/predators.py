from oop_hw.animals import Animal


class Predators(Animal):
    def __init__(self, age: int, name: str, gender: str, hunt_in_pride: bool):
        super().__init__(age, name, gender)
        self.hunt_in_pride = hunt_in_pride

    @staticmethod
    def feed_predator(food):
        return print(f' Your predator eat {food}')

    def feed_animal(self, food: str):
        return print(f' Your animal eat {food}')


lion = Predators(2, 'Simba', 'Male', True)



