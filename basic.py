from abc import ABC, abstractmethod
class Weapon:

    total_weapons = 0

    def __init__(self, name: str, ammo: int):
        self.name = name
        self.ammo = ammo
        Weapon.total_weapons += 1

class Soldier:
    def __init__(self, name: str, rank: str, weapon: Weapon):
        self.name = name
        self.rank = rank
        self.weapon = weapon

    def report(self):
        print(f"The soldier {self.name}. the rank is {self.rank}. his weapon is {self.weapon.name}")


class Unit:
    def __init__(self, unit_name: str, commander: Soldier, soldiers: list[Soldier]):
        self.unit_name = unit_name
        self.commander = commander
        self.soldiers = soldiers

    def briefing(self):
        print(f"unit {self.unit_name}. commander details: ")
        self.commander.report()


weapon1 = Weapon("tutu", 23)
weapon2 = Weapon("good", 32)
soldier1 = Soldier("Yossi", "t", weapon1)
soldier2 = Soldier("benny", "t", weapon1)
commander1 = Soldier("Mosh", "s", weapon2)

soldier1.report()
commander1.report()


class StrikeOption:
    def __init__(self, name: str, ammo: int):
        self.name = name
        self.ammo = ammo

    def strike(self):
        pass


class Drone(StrikeOption):
    def strike(self):
        print("The drone is striking")


class Tank(StrikeOption):
    def strike(self):
        print("The tank is striking")
