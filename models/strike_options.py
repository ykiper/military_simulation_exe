from abc import ABC, abstractmethod

class StrikeOption(ABC):
    def __init__(self, name: str, ammo: int):
        self.name = name
        self.ammo = ammo

    @abstractmethod
    def strike(self):
        pass


class Drone(StrikeOption):
    def strike(self):
        print("The drone is striking")


class Tank(StrikeOption):
    def strike(self):
        print("The tank is striking")