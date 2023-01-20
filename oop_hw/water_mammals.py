from oop_hw.animals import Animal


class Whales(Animal):
    def __init__(self, age: int, name: str, gender: str, live_in_groups: bool):
        super().__init__(age, name, gender)
        self.live_in_groups = live_in_groups

    @staticmethod
    def product_milk():
        return print(f' Your Whale products milf for children')

    def feed_animal(self, food: str):
        return print(f' Your animal eat {food}')


Whales(4, 'Polly', 'Female', True).product_milk()

