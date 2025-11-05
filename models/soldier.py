from weapon import Weapon
class Soldier:
    def __init__(self, name: str, rank: str, weapon: Weapon):
        self.name = name
        self.rank = rank
        self.weapon = weapon

    def report(self):
        print(f"The soldier {self.name}. the rank is {self.rank}. his weapon is {self.weapon.name}")
